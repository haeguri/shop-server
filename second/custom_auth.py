from django.conf import settings

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token
from rest_framework import exceptions, serializers
from rest_auth.serializers import TokenSerializer

from snippets.serializers import ProductLikeSerializer, ChannelFollowSerializer, BrandFollowSerializer, \
	IssueLikeSerializer

User = get_user_model()

class AuthTokenSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()

	def validate(self, attrs):
		email = attrs.get('email')
		password = attrs.get('password')

		if email and password:
			user = authenticate(email=email, password=password)

			if user:
				if not user.is_active:
					msg = _('User account is disabled.')
					raise exceptions.ValidationError(msg)
			else:
				msg = _('Unable to log in with provided credentials.')
				raise exceptions.ValidationError(msg)
		else:
			msg = _('Must include "email" and "password"')
			raise exceptions.ValidationError(msg)

		attrs['user'] = user
		return attrs


class LoginSerializer(AuthTokenSerializer):
	def validate(self, attrs):
		print("Test")
		attrs = super(LoginSerializer, self).validate(attrs)
		if 'rest_auth.auth' in settings.INSTALLED_APPS:
			from allauth.account import app_settings

			if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
				user = attrs['user']
				email_address = user.emailaddress_set.get(email=user.email)
				if not email_address.verified:
					raise serializers.ValidationError('E-mail is not verified.')
		return attrs


class UserDetailsSerializer(serializers.ModelSerializer):
	product_likes_of_user = ProductLikeSerializer(many=True, fields=('id', 'product',))
	channel_follows_of_user = ChannelFollowSerializer(many=True, fields=('id', 'channel',))
	brand_follows_of_user = BrandFollowSerializer(many=True, fields=('id', 'brand',))
	issue_likes_of_user = IssueLikeSerializer(many=True, fields=('id', 'issue',))

	class Meta:
		model = User
		fields = ('id', 'email', 'nickname', 'product_likes_of_user', 'issue_likes_of_user', 'channel_follows_of_user',
				  'brand_follows_of_user',)


# 로그인 요청이 성공적으로 처리되면 "TokenSerializer"가 "Token"을 직렬화해 response data로 보낸다.
# "TokenSerializer"를 상속받아 fields 속성에 'user' 필드를 추가했다.
class TokenSerializer(TokenSerializer):
	class Meta:
		model = Token
		fields = ('key', 'user')



from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.template import loader
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


class PasswordResetForm(forms.Form):
	email = forms.EmailField(label=_("Email"), max_length=254)

	def save(self, domain_override=None,
			 subject_template_name='auth/password_reset_subject.txt',
			 email_template_name='auth/password_reset_email.html',
			 use_https=False, token_generator=default_token_generator,
			 from_email=None, request=None, html_email_template_name=None):
		"""
        Generates a one-use only link for resetting password and sends to the
        user.
        """
		from django.core.mail import send_mail

		UserModel = get_user_model()
		email = self.cleaned_data["email"]
		active_users = UserModel._default_manager.filter(
			email__iexact=email, is_active=True)
		for user in active_users:
			# Make sure that no email is sent to a user that actually has
			# a password marked as unusable
			if not user.has_usable_password():
				continue
			if not domain_override:
				current_site = get_current_site(request)
				site_name = current_site.name
				domain = current_site.domain
			else:
				site_name = domain = domain_override
			c = {
				'email': user.email,
				'domain': domain,
				'site_name': site_name,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'user': user,
				'token': token_generator.make_token(user),
				'protocol': 'https' if use_https else 'http',
			}
			subject = loader.render_to_string(subject_template_name, c)
			# Email subject *must not* contain newlines
			subject = ''.join(subject.splitlines())
			email = loader.render_to_string(email_template_name, c)

			if html_email_template_name:
				html_email = loader.render_to_string(html_email_template_name, c)
			else:
				html_email = None
			# send_mail(subject, email, from_email, [user.email], html_message=html_email)

			from post_office import mail

			mail.send(
				[user.email],
				from_email,
				template='password_reset',
				context=c,
				priority='now',
			)

			# mail.send(
			# # 	['maphisto1@naver.com'],
			# # 	'haegyun821@gmail.com',
			# # 	subject='My email',
			# # 	message='Hi there!',
			# # 	html_message='Hi <strong>there</strong>!',
			# # 	priority='now',
			# # )

class PasswordResetSerializer(serializers.Serializer):

	email = serializers.EmailField()

	password_reset_form_class = PasswordResetForm

	def validate_email(self, value):
		# Create PasswordResetForm with the serializer
		self.reset_form = self.password_reset_form_class(data=self.initial_data)
		if not self.reset_form.is_valid():
			raise serializers.ValidationError('Error')
		return value

	def save(self):
		request = self.context.get('request')
		# Set some values to trigger the send_email method.
		opts = {
			'use_https': request.is_secure(),
			'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
			'request': request,
		}
		self.reset_form.save(**opts)







from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_username, user_field, valid_email_or_none


class SocialAccountAdapter(DefaultSocialAccountAdapter):
	def populate_user(self,
					  request,
					  sociallogin,
					  data):
		first_name = data.get('first_name')
		last_name = data.get('last_name')
		email = data.get('email')
		# name = data.get('name')
		user = sociallogin.user
		user_username(user, last_name + first_name)
		user_email(user, valid_email_or_none(email) or '')
		# name_parts = (name or '').partition(' ')
		# user_field(user, 'first_name', first_name or name_parts[0])
		# user_field(user, 'last_name', last_name or name_parts[2])
		return user


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin


class FacebookLogin(SocialLogin):
	adapter_class = FacebookOAuth2Adapter
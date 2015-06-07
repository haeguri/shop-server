from django.conf import settings

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token
from rest_framework import exceptions, serializers
from rest_auth.serializers import TokenSerializer

from snippets.serializers import ProductLikeSerializer, ChannelFollowSerializer, BrandFollowSerializer, IssueLikeSerializer

User = get_user_model()

class AuthTokenSerializer(serializers.Serializer):
	email 	 = serializers.EmailField()
	password = serializers.CharField()

	def validate(self, attrs):
		email 	= attrs.get('email')
		password= attrs.get('password')

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
		if 'rest_auth.registration' in settings.INSTALLED_APPS:
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
		fields = ('id', 'email', 'nickname', 'product_likes_of_user', 'issue_likes_of_user', 'channel_follows_of_user', 'brand_follows_of_user',)

# 로그인 요청이 성공적으로 처리되면 "TokenSerializer"가 "Token"을 직렬화해 response data로 보낸다.
# "TokenSerializer"를 상속받아 fields 속성에 'user' 필드를 추가했다.
class TokenSerializer(TokenSerializer):

    class Meta:
        model =  Token
        fields = ('key','user')


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin

class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter
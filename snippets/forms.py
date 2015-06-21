from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.template import loader
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.translation import ugettext_lazy as _

from snippets.models import Product, HashTagCategory

User = get_user_model()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'gender', 'name', 'price', 'pub_date', 'hash_tags')


    def clean(self):
        hash_tags = self.cleaned_data.get('hash_tags')
        if hash_tags is not None:
            input_categories = set(HashTagCategory.objects.filter(hashtag__id__in=hash_tags).filter(is_required=True))
            require_categories = set(HashTagCategory.objects.filter(is_required=True))

            if require_categories.difference(input_categories):
                difference_categories = list(require_categories.difference(input_categories))
                require_categories = ''
                for category in difference_categories:
                    require_categories = require_categories + ' ' + category.name

                raise forms.ValidationError("이런!!! 다음과 같은 필수 해쉬 태그를 입력하지 않았습니다. < %s >" % require_categories)

            return self.cleaned_data


class PasswordResetForm(forms.Form):
	email = forms.EmailField(label=_("Email"), max_length=254)

	def save(self, domain_override=None,
			 subject_template_name='auth/password_reset_subject.txt',
			 email_template_name='auth/password_reset_email.html',
			 use_https=False, token_generator=default_token_generator,
			 from_email=None, request=None, html_email_template_name=None):

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

from allauth.account.adapter import DefaultAccountAdapter

class MessageFreeAdapter(DefaultAccountAdapter):
    """
    django-allauth's `allauth.account.adapter.DefaultAccountAdapter` uses Django's messaging middleware to give feedback to users. When using django-rest-auth for auth/login JSON-REST requests a traceback is generated when the `HTTPRequest` is passed into `django.contrib.messages.add_messages` when a `Request` is expected:

    Exception Type: TypeError at /rest-auth/auth/
    Exception Value: add_message() argument must be an HttpRequest object, not &#39;Request&#39;.

    If messaging cannot be disabled (it is used by other applications) using this subclass
    disables messaging for allauth/django-rest-auth.

    In settings.py add ACCOUNT_ADAPTER = 'main.adapters.MessageFreeAdapter'
    """
    def add_message(self, request, level, message_template,
                    message_context={}, extra_tags=''):
        pass

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_username, valid_email_or_none

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

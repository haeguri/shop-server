from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework import pagination
from rest_framework.authtoken.models import Token
from rest_framework import exceptions, serializers

from rest_auth.serializers import TokenSerializer

from snippets.models import Gender, Product, ProductLike, Channel, Issue, IssueItem, \
	IssueLike, ChannelFollow, ProductImage, HashTag
from snippets.forms import PasswordResetForm

User = get_user_model()



from snippets.models import TestContent

class TestContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = TestContent
		fields = ('title', 'body',)



class DynamicFieldsModelSerializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		fields = kwargs.pop('fields', None)

		super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

		if fields:
			allowed = set(fields)
			existing = set(self.fields.keys())
			for field_name in existing - allowed:
				self.fields.pop(field_name)


class HashTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = HashTag
		fields = ('id', 'name')


class GenderSerializer(DynamicFieldsModelSerializer):
	class Meta:
		model = Gender
		fields = ('id', 'type')
		depth = 1


class ProductImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductImage
		fields = ('id', 'image', 'description')


class ProductSerializer(DynamicFieldsModelSerializer):
	images = ProductImageSerializer(many=True)

	def to_representation(self, instance):
		ret = super(ProductSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_like = ProductLike.objects.is_like(user_id, instance.id)
		ret['like'] = is_like

		return ret

	class Meta:
		model = Product
		fields = (
			'id', 'gender', 'name', 'pub_date', 'hash_tags', 'description', 'price', 'images',
			'product_likes_of_product')
		depth = 1


class IssueItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'images'))

	class Meta:
		model = IssueItem
		fields = ('id', 'issue', 'product', 'tip')


# "IssueSerializer"에서도 "ChannelSerializer" 보여줘야 하는데 "IssueSerializer"의 선언이 먼저 되어 있어 참조가 불가능.
# "SubChannelSerializer"는 "IssueSerializer"에서 참조하기 위한 "Channel"의 다른 "Serializer".
class SubChannelSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		ret = super(SubChannelSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = ChannelFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Channel
		fields = ('id', 'maker', 'introduce', 'profile', 'background', 'created', 'channel_follows_of_channel',
					'issues_of_channel')


class IssueSerializer(DynamicFieldsModelSerializer):
	issue_items_of_issue = IssueItemSerializer(many=True)
	channel = SubChannelSerializer(many=False)
	hash_tags = HashTagSerializer(many=True)

	def to_representation(self, instance):
		ret = super(IssueSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_like = IssueLike.objects.is_like(user_id, instance.id)
		ret['like'] = is_like

		return ret

	class Meta:
		model = Issue
		fields = (
			'id', 'channel', 'title', 'description', 'image', 'pub_date', 'hash_tags', 'view', 'issue_items_of_issue',
			'issue_likes_of_issue')


class ChannelSerializer(DynamicFieldsModelSerializer):
	issues_of_channel = IssueSerializer(many=True, fields=(
		'id', 'channel', 'hash_tags', 'title', 'image', 'pub_date', 'issue_likes_of_issue'))

	def to_representation(self, instance):
		ret = super(ChannelSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = ChannelFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Channel
		fields = ('id', 'maker', 'brief', 'introduce', 'profile', 'background', 'created', 'channel_follows_of_channel',
					'issues_of_channel')


class ProductLikeSerializer(DynamicFieldsModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'images'))

	class Meta:
		model = ProductLike
		fields = ('id', 'product', 'user')


class ChannelFollowSerializer(DynamicFieldsModelSerializer):
	channel = ChannelSerializer(many=False, fields=('id', 'maker', 'profile', 'channel_follows_of_channel',))

	class Meta:
		model = ChannelFollow
		fields = ('id', 'channel', 'user')


class IssueLikeSerializer(DynamicFieldsModelSerializer):
	issue = IssueSerializer(many=False, fields=('id', 'channel', 'title', 'image', 'pub_date',))

	class Meta:
		model = IssueLike
		fields = ('id', 'issue', 'user',)


class PaginationChannelSerializer(pagination.PaginationSerializer):
	class Meta:
		object_serializer_class = ChannelSerializer


class PaginationProductSerializer(pagination.PaginationSerializer):
	class Meta:
		object_serializer_class = ProductSerializer


class PaginationIssueSerializer(pagination.PaginationSerializer):
	class Meta:
		object_serializer_class = IssueSerializer


# 인증과 관련된 Serializer
# rest_auth 패키지의 일부를 커스텀한 것을 포함하고 있다.


# 로그인 요청이 성공적으로 처리되면 "TokenSerializer"가 "Token"을 직렬화해 response data로 보낸다.
# "TokenSerializer"를 상속받아 fields 속성에 'user' 필드를 추가했다.
class TokenSerializer(TokenSerializer):
	class Meta:
		model = Token
		fields = ('key', 'user')


# email과 pass
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


# 커스텀 AuthTokenSerializer를 상속받음.
class LoginSerializer(AuthTokenSerializer):
	def validate(self, attrs):
		attrs = super(LoginSerializer, self).validate(attrs)
		if 'rest_auth.auth' in settings.INSTALLED_APPS:
			from allauth.account import app_settings

			if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
				user = attrs['user']
				email_address = user.emailaddress_set.get(email=user.email)
				if not email_address.verified:
					raise serializers.ValidationError('E-mail is not verified.')
		return attrs


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


class UserDetailsSerializer(serializers.ModelSerializer):
	product_likes_of_user = ProductLikeSerializer(many=True, fields=('id', 'product',))
	channel_follows_of_user = ChannelFollowSerializer(many=True, fields=('id', 'channel',))
	issue_likes_of_user = IssueLikeSerializer(many=True, fields=('id', 'issue',))

	class Meta:
		model = User
		fields = ('id', 'email', 'nickname', 'product_likes_of_user', 'issue_likes_of_user', 'channel_follows_of_user')

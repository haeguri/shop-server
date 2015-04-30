from rest_framework import serializers
from snippets.models import Gender, Product, Brand, ProductLike, Channel, Issue, IssueItem, \
	IssueLike, ChannelFollow, BrandFollow, ProductSort, ProductImage, BrandInterview, \
	BrandFeed, HashTag, PubDay
from rest_framework import pagination

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
		fields = ('id', 'gender', 'brand', 'name', 'pub_date', 'hash_tags', 'description', 'price', 'images', 'product_likes_of_product')
		depth = 1

class BrandInterviewSerializer(serializers.ModelSerializer):

	class Meta:
		model = BrandInterview
		fields = ('id', 'image')

class BrandFeedSerializer(serializers.ModelSerializer):

	class Meta:
		model = BrandFeed
		fields = ('id', 'brand', 'title', 'pub_date', 'body', 'image')


class BrandSerializer(DynamicFieldsModelSerializer):
	products_of_brand = ProductSerializer(many=True)
	interviews = BrandInterviewSerializer(many=True)
	feeds = BrandFeedSerializer(many=True)

	def to_representation(self, instance):
		ret = super(BrandSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = BrandFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Brand
		fields = ('id', 'name', 'description', 'gender', 'products_of_brand', 'feeds', 'profile', 'background', 'web', 'interviews', 'address', 'brand_follows_of_brand')

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
		fields = ('id', 'name', 'introduce', 'web', 'profile', 'background', 'created', 'channel_follows_of_channel','issues_of_channel')

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
		fields = ('id', 'channel', 'title', 'description', 'image', 'pub_date', 'hash_tags', 'view', 'issue_items_of_issue', 'issue_likes_of_issue')


class PubDaySerializer(serializers.ModelSerializer):

	class Meta:
		model = PubDay
		fields = ('id', 'day')

class ChannelSerializer(DynamicFieldsModelSerializer):
	issues_of_channel = IssueSerializer(many=True, fields=('id', 'channel', 'hash_tags', 'title', 'image', 'pub_date', 'issue_likes_of_issue'))
	pub_days = PubDaySerializer(many=True)

	def to_representation(self, instance):
		ret = super(ChannelSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = ChannelFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Channel
		fields = ('id', 'name', 'pub_days','brief', 'introduce', 'web', 'profile', 'background', 'created', 'channel_follows_of_channel','issues_of_channel')

class ProductLikeSerializer(DynamicFieldsModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'images'))

	class Meta:
		model = ProductLike
		fields = ('id', 'product', 'user')


class BrandFollowSerializer(DynamicFieldsModelSerializer):
	brand = BrandSerializer(many=False, fields = ('id', 'name', 'gender', 'feeds', 'products_of_brand', 'profile', 'brand_follows_of_brand'))

	class Meta:
		model = BrandFollow
		fields = ('id', 'brand', 'user')

class ChannelFollowSerializer(DynamicFieldsModelSerializer):
	channel = ChannelSerializer(many=False, fields = ('id', 'name', 'profile', 'channel_follows_of_channel',))

	class Meta:
		model = ChannelFollow
		fields = ('id', 'channel', 'user')

class IssueLikeSerializer(DynamicFieldsModelSerializer):
	issue = IssueSerializer(many=False, fields=('id', 'channel', 'title', 'image', 'pub_date',))

	class Meta:
		model = IssueLike
		fields = ('id', 'issue', 'user',)

class ProductSortSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductSort
		fields = ('id', 'type',)


class PaginationChannelSerializer(pagination.PaginationSerializer):

	class Meta:
		object_serializer_class = ChannelSerializer

class PaginationProductSerializer(pagination.PaginationSerializer):

	class Meta:
		object_serializer_class = ProductSerializer

class PaginationIssueSerializer(pagination.PaginationSerializer):

	class Meta:
		object_serializer_class = IssueSerializer

class PaginationBrandFeedSerializer(pagination.PaginationSerializer):

	class Meta:
		object_serializer_class = BrandFeedSerializer
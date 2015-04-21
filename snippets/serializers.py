from rest_framework import serializers
from snippets.models import Gender, Product, Brand, ProductLike, Channel, Issue, IssueItem, \
	IssueLike, ChannelFollow, BrandFollow, ProductSort, ProductImage, BrandInterview
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
		field = ('id', 'brand', 'name', 'pub_date', 'description', 'price', 'images', 'product_likes_of_product')
		depth = 1

class PaginatedProductSerializer(pagination.PaginationSerializer):

	class Meta:
		object_serializer_class = ProductSerializer


class BrandInterviewSerializer(serializers.ModelSerializer):

	class Meta:
		model = BrandInterview
		fields = ('id', 'image')

class BrandSerializer(DynamicFieldsModelSerializer):
	products_of_brand = ProductSerializer(many=True)
	interviews = BrandInterviewSerializer(many=True)

	def to_representation(self, instance):
		ret = super(BrandSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = BrandFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Brand
		fields = ('id', 'name', 'introduce', 'gender', 'products_of_brand', 'image', 'background', 'web', 'interviews', 'address', 'brand_follows_of_brand')

class IssueItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'image'))

	class Meta:
		model = IssueItem
		fields = ('id', 'issue', 'product', 'tip')

class IssueSerializer(DynamicFieldsModelSerializer):
	issue_items_of_issue = IssueItemSerializer(many=True)

	def to_representation(self, instance):
		ret = super(IssueSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_like = IssueLike.objects.is_like(user_id, instance.id)
		ret['like'] = is_like

		return ret

	class Meta:
		model = Issue
		fields = ('id', 'channel', 'title', 'description', 'image', 'pub_date', 'issue_items_of_issue', 'issue_likes_of_issue')

class ChannelSerializer(DynamicFieldsModelSerializer):
	codies_of_channel = IssueSerializer(many=True, fields=('id', 'channel', 'title', 'image', 'pub_date', 'issue_likes_of_issue'))

	def to_representation(self, instance):
		ret = super(ChannelSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = ChannelFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Channel
		fields = ('id', 'name', 'introduce', 'web', 'image', 'background', 'created', 'channel_follows_of_channel','codies_of_channel')

class ProductLikeSerializer(DynamicFieldsModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'images'))

	class Meta:
		model = ProductLike
		fields = ('id', 'product', 'user')


class BrandFollowSerializer(DynamicFieldsModelSerializer):
	brand = BrandSerializer(many=False, fields = ('id', 'name', 'gender', 'products_of_brand', 'image', 'brand_follows_of_brand'))

	class Meta:
		model = BrandFollow
		fields = ('id', 'brand', 'user')

class ChannelFollowSerializer(DynamicFieldsModelSerializer):
	channel = ChannelSerializer(many=False, fields = ('id', 'name', 'image', 'channel_follows_of_channel',))

	class Meta:
		model = ChannelFollow
		fields = ('id', 'channel', 'user',)

class IssueLikeSerializer(DynamicFieldsModelSerializer):
	issue = IssueSerializer(many=False, fields=('id', 'channel', 'title', 'image', 'pub_date',))

	class Meta:
		model = IssueLike
		fields = ('id', 'issue', 'user',)

class ProductSortSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductSort
		fields = ('id', 'type',)

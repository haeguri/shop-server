from rest_framework import serializers
from snippets.models import Gender, Product, Brand, Tag, ProductLike, Cart, CartItem, Channel, Cody, CodyItem, \
	CodyLike, ChannelFollow, BrandFollow, CodyCategory, ProductSort, ProductImage, BrandInterview
from django.contrib.auth.models import User
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

class CodyCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = CodyCategory
		fields = ('id', 'name')

class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = ('id', 'gender', 'type')

class GenderSerializer(DynamicFieldsModelSerializer):

	class Meta:
		model = Gender
		fields = ('id', 'type', 'cody_categories_of_gender', 'tags_of_gender')
		depth = 1

class ProductImageSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductImage
		fields = ('id', 'image', 'description')

class ProductSerializer(DynamicFieldsModelSerializer):
	tag = TagSerializer(many=False)
	images = ProductImageSerializer(many=True)

	def to_representation(self, instance):
		ret = super(ProductSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_like = ProductLike.objects.is_like(user_id, instance.id)
		ret['like'] = is_like

		return ret

	class Meta:
		model = Product
		field = ('id', 'tag', 'brand', 'name', 'pub_date', 'description', 'price', 'images', 'product_likes_of_product')
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

class CodyItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'tag', 'image'))

	class Meta:
		model = CodyItem
		fields = ('id', 'cody', 'product', 'tip')

class CodySerializer(DynamicFieldsModelSerializer):
	cody_items_of_cody = CodyItemSerializer(many=True)
	cody_category = CodyCategorySerializer(many=False)

	def to_representation(self, instance):
		ret = super(CodySerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_like = CodyLike.objects.is_like(user_id, instance.id)
		ret['like'] = is_like

		return ret

	class Meta:
		model = Cody
		fields = ('id', 'channel', 'title', 'cody_category', 'description', 'image', 'pub_date', 'cody_items_of_cody', 'cody_likes_of_cody')

class ChannelSerializer(DynamicFieldsModelSerializer):
	codies_of_channel = CodySerializer(many=True, fields=('id', 'channel', 'title', 'image', 'pub_date', 'cody_likes_of_cody'))

	def to_representation(self, instance):
		ret = super(ChannelSerializer, self).to_representation(instance)
		user_id = self.context['request'].user.id
		is_follow = ChannelFollow.objects.is_follow(user_id, instance.id)
		ret['follow'] = is_follow

		return ret

	class Meta:
		model = Channel
		fields = ('id', 'name', 'introduce', 'web', 'address', 'image', 'background', 'created', 'channel_follows_of_channel','codies_of_channel')


class ItemReadSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'images'))

	class Meta:
		model = CartItem
		fields = ('id', 'product', 'cart', 'size', 'color', 'quantity')

class ItemWriteSerializer(serializers.ModelSerializer):

	class Meta:
		model = CartItem
		fields = ('id', 'product', 'cart', 'size', 'color', 'quantity')

class CartReadSerializer(serializers.ModelSerializer):
	cart_items_of_cart = ItemReadSerializer(many=True)

	class Meta:
		model = Cart
		fields = ('id', 'user', 'cart_items_of_cart', 'total_price', 'shipping', 'address')

class CartWriteSerializer(serializers.ModelSerializer):
	cart_items_of_cart = ItemWriteSerializer()

	class Meta:
		model = Cart
		fields = ('id', 'user', 'cart_items_of_cart', 'total_price', 'shipping', 'address')

class ProductLikeSerializer(DynamicFieldsModelSerializer):
	product = ProductSerializer(many=False, fields=('id', 'tag', 'name', 'price', 'images'))

	class Meta:
		model = ProductLike
		fields = ('id', 'product', 'user')


class BrandFollowSerializer(DynamicFieldsModelSerializer):
	brand = BrandSerializer(many=False, fields = ('id', 'name', 'gender', 'products_of_brand', 'image', 'brand_follows_of_brand'))

	class Meta:
		model = BrandFollow
		fields = ('id', 'brand', 'user')

class ChannelFollowSerializer(DynamicFieldsModelSerializer):
	channel = ChannelSerializer(many=False, fields = ('id', 'name', 'image', 'channel_follows_of_channel'))

	class Meta:
		model = ChannelFollow
		fields = ('id', 'channel', 'user')

class CodyLikeSerializer(DynamicFieldsModelSerializer):
	cody = CodySerializer(many=False, fields=('id', 'channel', 'title', 'image', 'pub_date'))

	class Meta:
		model = CodyLike
		fields = ('id', 'cody', 'user')

class UserSerializer(serializers.ModelSerializer):

	cart = CartReadSerializer(many=False)
	product_likes_of_user = ProductLikeSerializer(many=True, fields=('id', 'product',))
	channel_follows_of_user = ChannelFollowSerializer(many=True, fields=('id', 'channel'))
	brand_follows_of_user = BrandFollowSerializer(many=True, fields=('id', 'brand'))
	cody_likes_of_user = CodyLikeSerializer(many=True, fields=('id', 'cody'))

	class Meta:
		model = User
		fields = ('id', 'username','email', 'cart', 'product_likes_of_user', 'cody_likes_of_user', 'channel_follows_of_user', 'brand_follows_of_user')

class ProductSortSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductSort
		fields = ('id', 'type')

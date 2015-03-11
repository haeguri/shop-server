from rest_framework import serializers
from snippets.models import Product, Category, Designer, Tag, Like, Cart, CartItem, Channel, Cody, CodyItem, \
	CodyLike, ChannelFollow, DesignerFollow
from django.contrib.auth.models import User
from rest_framework import pagination

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ('id', 'gender', 'type', 'tags_of_category')
		depth = 1

class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = ('id', 'category', 'name')

class DesignerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Designer
		fields = ('id', 'name', 'intro', 'image', 'image', 'web', 'address')

class DesignerFollowSerializer(serializers.ModelSerializer):

	designer = DesignerSerializer(serializers.ModelSerializer)

	class Meta:
		model = DesignerFollow
		fields = ('id', 'designer', 'user', 'whether_follow')

class ProductSerializer(serializers.ModelSerializer):

	likes_of_product = serializers.SerializerMethodField()
	tag = TagSerializer(many=False)
	designer = DesignerSerializer(many=False)

	def get_likes_of_product(self, product):
		query_set = Like.objects.filter(whether_like=True, product=product)
		serializer = LikeSerializer(instance=query_set, many=True)

		return serializer.data

	class Meta:
		model = Product
		fields = ('id', 'tag', 'designer', 'name', 'pub_date', 'description', 'price', 'image', 'likes_of_product')

class PaginatedProductSerializer(pagination.PaginationSerializer):

	class Meta:
		object_serializer_class = ProductSerializer


class ChannelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Channel
		fields = ('id', 'name', 'intro', 'web', 'address', 'image', 'created', 'channel_follows_of_channel')
		depth=1

class ChannelFollowSerializer(serializers.ModelSerializer):
	channel = ChannelSerializer(many=False)

	class Meta:
		model = ChannelFollow
		fields = ('id', 'whether_follow', 'channel', 'user')

class CodyItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False)

	class Meta:
		model = CodyItem
		fields = ('id', 'cody', 'product', 'tip')

class CodySerializer(serializers.ModelSerializer):
	cody_items_of_cody = CodyItemSerializer(many=True)

	class Meta:
		model = Cody
		fields = ('id', 'channel', 'title', 'desc', 'image', 'pub_date', 'cody_items_of_cody')

class CodyLikeSerializer(serializers.ModelSerializer):

	class Meta:
		model = CodyLike
		fields = ('id', 'whether_like', 'cody', 'user')

class ItemReadSerializer(serializers.ModelSerializer):
	product = ProductSerializer(many=False)

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

class UserSerializer(serializers.ModelSerializer):
	cart = CartReadSerializer(many=False)
	likes_of_user = serializers.SerializerMethodField()
	channel_follows_of_user = serializers.SerializerMethodField()
	designer_follows_of_user = serializers.SerializerMethodField()
	cody_likes_of_user = serializers.SerializerMethodField()

	"""
	def get_cart(self, user):
		instance = Cart.objects.get(user=user)
		serializer = CartReadSerializer(instance = instance)

		return serializer.data
	"""

	def get_likes_of_user(self, user):
		query_set = Product.objects.filter(likes_of_product__user=user, likes_of_product__whether_like=True)
		serializer =  ProductSerializer(instance=query_set, many=True)

		return serializer.data

	def get_channel_follows_of_user(self, user):
		query_set = Channel.objects.filter(channel_follows_of_channel__user=user, channel_follows_of_channel__whether_follow=True)
		serializer = ChannelSerializer(instance=query_set, many=True)

		return serializer.data

	def get_designer_follows_of_user(self, user):
		query_set = Designer.objects.filter(designer_follows_of_designer__user=user, designer_follows_of_designer__whether_follow=True)
		serializer =  DesignerSerializer(instance=query_set, many=True)

		return serializer.data

	def get_cody_likes_of_user(self, user):
		query_set = Cody.objects.filter(cody_likes_of_cody__user=user, cody_likes_of_cody__whether_like=True)
		serializer =  CodySerializer(instance=query_set, many=True)

		return serializer.data

	class Meta:
		model = User
		fields = ('id', 'username','email', 'cart', 'likes_of_user', 'cody_likes_of_user', 'channel_follows_of_user', 'designer_follows_of_user')




class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Like
		fields = ('whether_like', 'product', 'user')
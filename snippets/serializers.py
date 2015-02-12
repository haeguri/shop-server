from rest_framework import serializers
from snippets.models import Product, Category, Like, Cart, CartItem
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ('id', 'gender', 'name')

class ProductSerializer(serializers.ModelSerializer):
	likes = serializers.SerializerMethodField()

	def get_likes(self, product):
		query_set = Like.objects.filter(whether_like=True, product=product)
		serializer = LikeSerializer(instance=query_set, many=True)

		return serializer.data

	class Meta:
		model = Product
		fields = ('id', 'category', 'name', 'pub_date', 'description', 'price', 'image', 'likes')


class ItemReadSerializer(serializers.ModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = CartItem
		fields = ('id', 'product', 'cart', 'size', 'color', 'quantity')

class ItemWriteSerializer(serializers.ModelSerializer):

	class Meta:
		model = CartItem
		fields = ('id', 'product', 'cart', 'size', 'color', 'quantity')

class CartReadSerializer(serializers.ModelSerializer):
	items = ItemReadSerializer(many=True)

	class Meta:
		model = Cart
		fields = ('id', 'user', 'items', 'total_price', 'shipping', 'address')

class CartWriteSerializer(serializers.ModelSerializer):
	items = ItemWriteSerializer()

	class Meta:
		model = Cart
		fields = ('id', 'user', 'items', 'total_price', 'shipping', 'address')




class UserSerializer(serializers.ModelSerializer):
	likes = serializers.SerializerMethodField()

	def get_likes(self, user):
		query_set = Product.objects.filter(likes__user=user, likes__whether_like=True)
		serializer =  ProductSerializer(instance=query_set, many=True)

		return serializer.data

	class Meta:
		model = User
		fields = ('id', 'username','email', 'likes')

class LikeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Like
		fields = ('whether_like', 'product', 'user')
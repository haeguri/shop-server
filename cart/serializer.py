from rest_framework import serializers
from cart.models import CartItem, Cart
from snippets.serializers import ProductSerializer

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

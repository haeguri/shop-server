from rest_framework import serializers
from cart.models import CartItem, Cart
from snippets.serializers import ProductSerializer
from snippets.models import Product


class ItemReadSerializer(serializers.ModelSerializer):
	#product = ProductSerializer(many=False, fields=('id', 'name', 'price', 'images'))

	product = serializers.SerializerMethodField()


	def get_product(self, instance):

		product = Product.objects.get(cart_items_of_product__id=instance.id)
		serializer = ProductSerializer(product, many=False,  fields=('id', 'name', 'price', 'images'), context=self.context)

		return serializer.data

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

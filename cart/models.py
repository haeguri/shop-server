from django.db import models
from django.contrib.auth.models import User
from snippets.models import Product

class CartManager(models.Manager):

	def get_or_create(self, user_id):
		try:
			return Cart.objects.get(user__id = user_id)
		except:
			user = User.objects.get(id=user_id)
			return Cart.objects.create(user=user)

class Cart(models.Model):
	user = models.OneToOneField(User)
	shipping = models.IntegerField(default=2500)
	total_price = models.IntegerField(default=0)
	address = models.TextField(max_length=100)

	objects = CartManager()

# Will be prevent to duplicated.
class CartItem(models.Model):

	product = models.ForeignKey(Product, related_name='cart_items_of_product')
	cart = models.ForeignKey(Cart, related_name='cart_items_of_cart')
	size = models.CharField(max_length=10, null=True) # will be fixed!!!!!!
	color = models.CharField(max_length=10, null=True) # will be fixed!!!!!!
	quantity = models.IntegerField(null=True)
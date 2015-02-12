from django.contrib.auth.models import User
from django.db import models

COMMON_SIZES = (
	('S', 'Small'),
	('M', 'Medium'),
	('L', 'Large'),
	('XL', 'XLarge'),
)

class Gender(models.Model):
	type = models.CharField(max_length=5)

	def __str__(self):
		return self.type

class Channel(models.Model):
	user = models.ManyToManyField(User, related_name='channels')
	jacket = models.ImageField(upload_to='upload/channel/jacket', default='')
	designer = models.ImageField(upload_to='upload/channel/designer', default='')
	pub_date = models.DateTimeField('date published')


class CategoryManager(models.Manager):
	def get_men_category(self):
		try:
			category = Category.objects.filter(gender__type='Men')
			return category
		except:
			print("exception in CategoryManager get_men_category")
			return []

	def get_women_category(self):
		try:
			category = Category.objects.filter(gender__type='Women')
			return category
		except:
			print("exception in CategoryManager get_women_category")
			return []

class Category(models.Model):
	gender = models.ForeignKey(Gender, related_name='categories')
	name = models.CharField(max_length=20)

	objects = CategoryManager()

	def __str__(self):
		return self.name

class ProductManager(models.Manager):

	def init_like(self, user_id):
		try:
			user_like_list = Like.objects.filter(user_id=user_id, whether_like=True)
			like_id_list = []

			for item in user_like_list:
				like_id_list.append(item.product.id)

			return like_id_list
		except:
			print("except init_like!!")
			return []

	def get_like_product(self, user_id):
		try:
			user_like_list = Like.objects.filter(user_id=user_id)
			user_product_list = []

			for like in user_like_list:
				user_product_list.append(like.id)

			return Product.objects.filter(id__in=user_product_list)

		except:
			return []


class Product(models.Model):
	channel = models.ForeignKey(Channel, related_name='products', blank=True)
	category = models.ForeignKey(Category, related_name='products')
	pub_date = models.DateTimeField('date published')
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=100)
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to='upload')

	objects = ProductManager()

	def __str__(self):
		return self.name

class LikeManager(models.Manager):

	def get_or_create(self, user, product):
		try:
			return Like.objects.get(user=user, product=product)

		except:
			return Like.objects.create(user=user, product=product)

	def like_count(self, product):
		try:
			return Like.objects.filter(product = product, whether_like = True).count()
		except:
			return 0


class Like(models.Model):
	whether_like = models.BooleanField(default=False)
	product = models.ForeignKey(Product, related_name='likes')
	user = models.ForeignKey(User, related_name='likes')

	objects = LikeManager()


class CartManager(models.Manager):

	def get_or_create(self, user_id):
		try:
			cart = Cart.objects.get(user__id = user_id)
			return cart
		except:
			user = User.objects.get(id=user_id)
			cart = Cart.objects.create(user=user)
			return cart

class Cart(models.Model):
	user = models.OneToOneField(User)
	shipping = models.IntegerField(default=2500)
	total_price = models.IntegerField(default=0)
	address = models.TextField(max_length=100)

	objects = CartManager()


class CartItemManager(models.Manager):
	pass

class CartItem(models.Model):
	product = models.ForeignKey(Product, related_name='items')
	cart = models.ForeignKey(Cart, related_name='items')
	size = models.CharField(null=True, max_length=10)
	color = models.CharField(null=True, max_length=10)
	quantity = models.IntegerField(null=True)

	objects = CartItemManager()
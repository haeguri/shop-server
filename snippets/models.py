from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address = models.TextField(max_length=200, blank=True)

class Gender(models.Model):
	type = models.CharField(max_length=8)

	def __str__(self):
		return self.type

class CategoryManager(models.Manager):

	def get_category_list(self, gender_id):
		return Category.objects.filter(gender = gender_id)

class Category(models.Model):
	gender = models.ForeignKey(Gender, related_name='categories_of_gender', blank=True, null=True)
	type = models.CharField(max_length=10, default='')

	objects = CategoryManager()

	def __str__(self):
		return self.gender.type + ' / ' + self.type

class TagManager(models.Manager):

	def get_tags_of_brand(self, brand_id):
		tags_of_brand = Brand.objects.get(id=brand_id).products_of_brand.values_list('tag',flat=True)
		return Tag.objects.filter(id__in=tags_of_brand)

class Tag(models.Model):
	gender = models.ForeignKey(Gender, related_name='tags_of_gender', blank=True, null=True)
	category = models.ForeignKey(Category, related_name='tags_of_category', blank=True, null=True)
	name = models.CharField(max_length=20, default='')

	objects = TagManager()

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class CodyCategory(models.Model):
	gender = models.ForeignKey(Gender, related_name='cody_categories_of_gender', blank=True, null=True)
	name = models.CharField(max_length=20, default='')

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class BrandManager(models.Manager):

	def get_without_follow(self, user_id, gender_id):
		if user_id is not None:
			follow_brands = BrandFollow.objects.filter(user=user_id)

			return Brand.objects.exclude(brand_follows_of_brand__in=follow_brands).filter(gender=gender_id)
		else: # anonymous user
			return Brand.objects.all()

class Brand(models.Model):
	user = models.OneToOneField(User)
	gender = models.ForeignKey(Gender, max_length=5, related_name='brands_of_gender', blank=True, null=True)
	name = models.CharField(max_length=20)
	intro = models.TextField(max_length=200, blank=True)
	image = models.ImageField(upload_to='upload/brand', default='')
	background = models.ImageField(upload_to='upload/brand/background', default='', blank=True)
	web = models.CharField(max_length=50, blank=True)
	address = models.CharField(max_length=200, blank=True)

	objects = BrandManager()

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class BrandFollowManager(models.Manager):

	def is_follow(self, user_id, brand_id):
		try:
			return BrandFollow.objects.get(user=user_id, brand=brand_id) is not None
		except:
			return False


class BrandFollow(models.Model):
	user = models.ForeignKey(User, related_name="brand_follows_of_user")
	brand = models.ForeignKey(Brand, related_name="brand_follows_of_brand", unique=True)

	objects = BrandFollowManager()

class Product(models.Model):
	brand = models.ForeignKey(Brand, related_name='products_of_brand', blank=True, null=True)
	tag = models.ForeignKey(Tag, related_name='products_of_tag', blank=True, null=True)
	pub_date = models.DateTimeField('date published', default=datetime.now())
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=100)
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to='upload')

	def __str__(self):
		return self.name + '(' + self.tag.gender.type + ')'

class AdminChannel(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='channel')

class Channel(models.Model):
	name = models.CharField(max_length=30)
	intro = models.TextField(max_length=200)
	image = models.ImageField(upload_to='channel')
	background = models.ImageField(upload_to='channel/background', blank=True, null=True)
	web = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	created = models.DateTimeField('date created', default=datetime.now)

	def __str__(self):
		return self.name

class ChannelFollowManager(models.Manager):

	def is_follow(self, user_id, channel_id):
		try:
			return ChannelFollow.objects.get(user=user_id, channel=channel_id) is not None
		except:
			return False


class ChannelFollow(models.Model):
	user = models.ForeignKey(User, related_name="channel_follows_of_user")
	channel = models.ForeignKey(Channel, related_name="channel_follows_of_channel", unique=True)

	objects = ChannelFollowManager()

class CodyManager(models.Manager):
	def get_without_follow(self, user_id):

		try:
			follow_channels = ChannelFollow.objects.filter(user=user_id).values_list('channel', flat=True)

			return Cody.objects.exclude(channel__in=follow_channels)
		# no one channel of following
		except:
			return Cody.objects.all()

	def get_codies_of_category(self, category_id):
		return Cody.objects.filter(cody_category=category_id)

class Cody(models.Model):
	channel = models.ForeignKey(Channel, related_name='codies_of_channel')
	cody_category = models.ForeignKey(CodyCategory, related_name="codies_of_cody_category", blank=True, null=True)
	title = models.CharField(max_length=15)
	desc = models.TextField(max_length=200)
	image = models.ImageField(upload_to='channel/channel_cody')
	pub_date = models.DateTimeField('date published', default=datetime.now())

	objects = CodyManager()

	def __str__(self):
		return self.title

class CodyLikeManager(models.Manager):

	def is_like(self, user_id, cody_id):
		try:
			return CodyLike.objects.get(user=user_id, cody=cody_id) is not None
		except:
			return False


class CodyLike(models.Model):
	cody = models.ForeignKey(Cody, related_name='cody_likes_of_cody', unique=True)
	user = models.ForeignKey(User, related_name='cody_likes_of_user')

	objects = CodyLikeManager()

class CodyItem(models.Model):
	cody = models.ForeignKey(Cody, related_name='cody_items_of_cody')
	product = models.ForeignKey(Product, related_name='cody_items_of_product')
	tip = models.CharField(max_length=50)

	def __str__(self):
		return self.product.name + '(' + self.product.tag.gender.type + ')'

class ProductLikeManager(models.Manager):

	def is_like(self, user_id, product_id):
		try:
			return ProductLike.objects.get(user=user_id, product=product_id) is not None
		except:
			return False


class ProductLike(models.Model):
	product = models.ForeignKey(Product, related_name='product_likes_of_product')
	user = models.ForeignKey(User, related_name='product_likes_of_user')

	objects = ProductLikeManager()


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

class CartItem(models.Model):
	product = models.ForeignKey(Product, related_name='cart_items_of_product')
	cart = models.ForeignKey(Cart, related_name='cart_items_of_cart')
	size = models.CharField(null=True, max_length=10)
	color = models.CharField(null=True, max_length=10)
	quantity = models.IntegerField(null=True)
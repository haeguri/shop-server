from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone
import os

class TestHashTagCategory(models.Model):
	name = models.CharField(unique=True, max_length=10, blank=False)
	is_required = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class TestHashTag(models.Model):
	name = models.CharField(unique=True, max_length=10, blank=False)
	category = models.ForeignKey(TestHashTagCategory, blank=False, default='')

	def __str__(self):
		if self.category.is_required==True:
			return '['+ self.category.name+']' + self.name
		else:
			return self.name

	class Meta:
		ordering = ('category',)

class TestModel(models.Model):
	name = models.CharField(max_length=10, unique=True, blank=False)
	hash_tags = models.ManyToManyField(TestHashTag)

	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address = models.TextField(max_length=200, blank=True)

class Gender(models.Model):
	type = models.CharField(max_length=8)

	def __str__(self):
		return self.type

class TagManager(models.Manager):

	def get_tags_of_brand(self, brand_id):
		tags_of_brand = Brand.objects.get(id=brand_id).products_of_brand.values_list('tag',flat=True)
		return Tag.objects.filter(id__in=tags_of_brand)

class Tag(models.Model):

	gender = models.ForeignKey(Gender, related_name='tags_of_gender', blank=True, null=True)
	type = models.CharField(max_length=20, default='')
	slug = models.SlugField(unique=True,
							help_text="Displayed tags depends on the order of priority.. like Outer->Jeans->Bags")

	objects = TagManager()

	def __str__(self):
		return self.type + '(' + self.gender.type + ')'

	class Meta:
		ordering = ('slug',)

class ProductSort(models.Model):
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type

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
	introduce = models.TextField(max_length=200, blank=True)
	image = models.ImageField(upload_to='upload/brand', default='')
	background = models.ImageField(upload_to='upload/brand/background', default='')
	web = models.URLField(blank=True)
	address = models.CharField(max_length=200, blank=True)

	objects = BrandManager()

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class BrandInterview(models.Model):
	brand = models.ForeignKey(Brand, related_name='interviews')

	def get_upload_path(instance, filename):
		path = os.path.join("upload/brand/%s/interviews/" % instance.brand.name, filename)
		print("path is ", path.replace(" ", "_"))
		return path

	image = models.ImageField(upload_to=get_upload_path)

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
	tag = models.ForeignKey(Tag, related_name='products_of_tag', null=True)
	pub_date = models.DateTimeField('date published', default=timezone.localtime(timezone.now()))
	name = models.CharField(unique=True, max_length=15)
	description = models.TextField(max_length=100, default='')
	price = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images')
	description = models.TextField(max_length=1000, default='', blank=True)

	def get_upload_path(instance, filename):
		path = os.path.join("product/%s/" % instance.product.name, filename)
		return path

	image = models.ImageField(upload_to=get_upload_path)

class Channel(models.Model):
	name = models.CharField(unique=True, max_length=30)
	introduce = models.TextField(max_length=200)
	image = models.ImageField(upload_to='channel')
	background = models.ImageField(upload_to='channel/background', default='')
	web = models.URLField()
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
		# no one channel with following
		except:
			return Cody.objects.all()

	def get_codies_of_category(self, category_id):
		return Cody.objects.filter(cody_category=category_id)

class Cody(models.Model):

	DAY_OF_WHICHDAY_CHOICES = (
		('MO', 'Monday'),
		('TU', 'Tuesday'),
		('WE', 'Wednesday'),
		('TH', 'Thursday'),
		('FR', 'Friday'),
		('SA', 'Saturday'),
	)

	channel = models.ForeignKey(Channel, related_name='codies_of_channel')
	cody_category = models.ForeignKey(CodyCategory, related_name="codies_of_cody_category", blank=True, null=True)
	title = models.CharField(unique=True, max_length=20)
	description = models.TextField(max_length=200, default='')
	image = models.ImageField(upload_to='channel/channel_cody', default='')
	which_day = models.CharField(max_length=2, choices=DAY_OF_WHICHDAY_CHOICES, default='MO')
	pub_date = models.DateTimeField('date published', default=timezone.localtime(timezone.now()))

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

# Will be prevent to duplicated.
class CartItem(models.Model):

	product = models.ForeignKey(Product, related_name='cart_items_of_product')
	cart = models.ForeignKey(Cart, related_name='cart_items_of_cart')
	size = models.CharField(max_length=10, null=True) # will be fixed!!!!!!
	color = models.CharField(max_length=10, null=True) # will be fixed!!!!!!
	quantity = models.IntegerField(null=True)

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import shutil

@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	from second.settings import BASE_DIR
	shutil.rmtree(os.path.join('%s/media/product/' % BASE_DIR, instance.name))

@receiver(pre_delete, sender=ProductImage)
def product_image_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()

@receiver(pre_delete, sender=BrandInterview)
def brand_interview_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()


@receiver(pre_delete, sender=Brand)
def brand_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()
	instance.background.delete()

@receiver(pre_delete, sender=Channel)
def channel_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()
	instance.background.delete()

@receiver(pre_delete, sender=Cody)
def cody_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()

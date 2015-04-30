from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone
from snippets.hangul import separate
import os

class HashTagCategory(models.Model):
	name = models.CharField(unique=True, max_length=10, blank=False)
	is_required = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class HashTagManager(models.Manager):

	def get_pop_hashtag(self):
		HashTag.objects.filter()
		pass

class HashTag(models.Model):
	name = models.CharField(unique=True, max_length=10, blank=False)
	#separated_name = models.CharField(max_length=100)
	category = models.ForeignKey(HashTagCategory, blank=False)

	objects =HashTagManager()

#	def separate_char(self):
#		separate(self.name)

#	def save(self, *args, **kwargs):
#		if not self.subject_init:
#			self.separated_name = self.subject_initials()
#		super(HashTag, self).save(*args, **kwargs)

	def __str__(self):
		if self.category.is_required==True:
			return '['+ self.category.name+']' + self.name
		else:
			return self.name

	class Meta:
		ordering = ('category',)

class Gender(models.Model):
	type = models.CharField(max_length=8)

	def __str__(self):
		return self.type

class ProductSort(models.Model):
	type = models.CharField(max_length=10)

	def __str__(self):
		return self.type

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
	description = models.TextField(max_length=200, blank=True)
	profile = models.ImageField(upload_to='upload/brand', default='')
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
		return path

	image = models.ImageField(upload_to=get_upload_path)

class BrandFeed(models.Model):
	brand = models.ForeignKey(Brand, related_name='feeds')
	title = models.CharField(max_length=20, blank=False)
	body = models.TextField(max_length=200, blank=True)
	pub_date = models.DateTimeField('date published', default=timezone.localtime(timezone.now()))

	def get_upload_path(instance, filename):
		path = os.path.join("upload/brand/%s/feed/" % instance.brand.name, filename)
		return path

	image = models.ImageField(upload_to=get_upload_path)

	class Meta:
		ordering = ('-pub_date',)


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
	gender = models.ForeignKey(Gender, blank=False, null=True)
	hash_tags = models.ManyToManyField(HashTag, related_name='products', blank=False)
	brand = models.ForeignKey(Brand, related_name='products_of_brand', blank=True, null=True)
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


class PubDay(models.Model):
	DAY_OF_WHICHDAY_CHOICES = (
		('월', '월요일'),
		('화', '화요일'),
		('수', '수요일'),
		('목', '목요일'),
		('금', '금요일'),
		('토', '토요일'),
	)

	day = models.CharField(blank=True, max_length=2, choices=DAY_OF_WHICHDAY_CHOICES, default='월')

	def __str__(self):

		return self.day

class ChannelManager(models.Manager):
	def as_json(self, channel):
		print("channel.background", dir(channel.background.path))
		return dict(
			name=channel.name, which_day=channel.which_day, created=channel.created, profile=channel.profile,
			background=channel.background, channel_follows_of_channel=channel.channel_follows_of_channel
		)

class Channel(models.Model):

	name = models.CharField(unique=True, max_length=10)
	brief = models.CharField(max_length=10, default='', blank=False)
	pub_days = models.ManyToManyField(PubDay, blank=True)
	created = models.DateTimeField('date created', default=datetime.now)
	introduce = models.TextField(max_length=200)
	profile = models.ImageField(upload_to='channel')
	background = models.ImageField(upload_to='channel/background', default='')
	web = models.URLField(blank=True)
	address = models.CharField(max_length=20, default='', blank=True)

	objects = ChannelManager()

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

class IssueManager(models.Manager):
	def get_without_follow(self, user_id):

		try:
			follow_channels = ChannelFollow.objects.filter(user=user_id).values_list('channel', flat=True)

			return Issue.objects.exclude(channel__in=follow_channels)
		# no one channel with following
		except:
			return Issue.objects.all()

class Issue(models.Model):

	pub_date = models.DateTimeField('date published', default=timezone.localtime(timezone.now()))
	hash_tags = models.ManyToManyField(HashTag, related_name='issues')
	channel = models.ForeignKey(Channel, related_name='issues_of_channel')
	title = models.CharField(unique=True, max_length=10)
	description = models.TextField(max_length=200, default='')
	image = models.ImageField(upload_to='channel/channel_issue', default='')
	view = models.PositiveIntegerField(default=0)

	objects = IssueManager()

	def __str__(self):
		return self.title

class IssueLikeManager(models.Manager):

	def is_like(self, user_id, issue_id):
		try:
			return IssueLike.objects.get(user=user_id, issue=issue_id) is not None
		except:
			return False


class IssueLike(models.Model):
	issue = models.ForeignKey(Issue, related_name='issue_likes_of_issue', unique=True)
	user = models.ForeignKey(User, related_name='issue_likes_of_user')

	objects = IssueLikeManager()

class IssueItem(models.Model):
	issue = models.ForeignKey(Issue, related_name='issue_items_of_issue')
	product = models.ForeignKey(Product, related_name='issue_items_of_product')
	tip = models.CharField(max_length=50)

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

@receiver(pre_delete, sender=Issue)
def issue_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()

@receiver(pre_delete, sender=BrandFeed)
def brandfeed_delete(sender, instance, **kwargs):
	# Pass false so FileField doesn't save the model.
	instance.image.delete()


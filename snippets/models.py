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

	def get_tags(self, gender_id):
		return Tag.objects.filter(gender=gender_id)

	def get_tags_of_designer(self, designer_id):
		tags_of_designer = Designer.objects.get(id=designer_id).products_of_designer.values_list('tag',flat=True)
		return Tag.objects.filter(id__in=tags_of_designer)

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
	image = models.ImageField(upload_to='upload/cody/category', default='')

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class DesignerManager(models.Manager):

	def get_without_follow(self, user_id, gender_id):
		follow_designers = DesignerFollow.objects.filter(user=user_id, whether_follow=True)

		return Designer.objects.exclude(designer_follows_of_designer__in=follow_designers).filter(gender=gender_id)

class Designer(models.Model):
	user = models.OneToOneField(User)
	gender = models.ForeignKey(Gender, max_length=5, related_name='designers_of_gender', blank=True, null=True)
	name = models.CharField(max_length=20)
	intro = models.TextField(max_length=200, blank=True)
	image = models.ImageField(upload_to='upload/designer', default='')
	background = models.ImageField(upload_to='upload/designer/background', default='')
	web = models.CharField(max_length=50, blank=True)
	address = models.CharField(max_length=200, blank=True)

	objects = DesignerManager()

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class DesignerFollowManager(models.Manager):

	def get_or_create(self, user_id, designer_id):
		user = User.objects.get(id=user_id)
		designer = Designer.objects.get(id=designer_id)

		try:
			follow = DesignerFollow.objects.get(user=user, designer=designer)
		except:
			follow = DesignerFollow.objects.create(user=user, designer=designer)

		follow.whether_follow = not follow.whether_follow
		follow.save()

		return Designer.objects.filter(designer_follows_of_designer__user=user_id, designer_follows_of_designer__whether_follow=True)

class DesignerFollow(models.Model):
	user = models.ForeignKey(User, related_name="designer_follows_of_user")
	designer = models.ForeignKey(Designer, related_name="designer_follows_of_designer")
	whether_follow = models.BooleanField(default=False)

	objects = DesignerFollowManager()

class Product(models.Model):
	designer = models.ForeignKey(Designer, related_name='products_of_designer', blank=True, null=True)
	tag = models.ForeignKey(Tag, related_name='products_of_tag', blank=True, null=True)
	pub_date = models.DateTimeField('date published', default=datetime.now)
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
	web = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	created = models.DateTimeField('date created', default=datetime.now)

	def __str__(self):
		return self.name

class ChannelFollowManager(models.Manager):

	def get_or_create(self, user_id, channel_id):
		user = User.objects.get(id=user_id)
		channel = Channel.objects.get(id=channel_id)

		try:
			follow = ChannelFollow.objects.get(user=user, channel=channel)
		except:
			follow = ChannelFollow.objects.create(user=user, channel=channel)

		follow.whether_follow = not follow.whether_follow
		follow.save()

		return Channel.objects.filter(channel_follows_of_channel__user=user_id, channel_follows_of_channel__whether_follow=True)

class ChannelFollow(models.Model):
	channel = models.ForeignKey(Channel, related_name="channel_follows_of_channel")
	user = models.ForeignKey(User, related_name="channel_follows_of_user")
	whether_follow = models.BooleanField(default=False)

	objects = ChannelFollowManager()

class CodyManager(models.Manager):
	def get_without_follow(self, user_id):

		try:
			follow_channels = ChannelFollow.objects.filter(user=user_id, whether_follow=True).values_list('channel', flat=True)

			return Cody.objects.exclude(channel__in=follow_channels)
		# no one channel of following
		except:
			return Cody.objects.all()

	def get_codies_of_category(self, category_id):
		return Cody.objects.filter(cody_category=category_id)

class Cody(models.Model):
	channel = models.ForeignKey(Channel, related_name='codies_of_channel')
	cody_category = models.ForeignKey(CodyCategory, related_name="codies_of_cody_category", blank=True, null=True)
	title = models.CharField(max_length=30)
	desc = models.TextField(max_length=200)
	image = models.ImageField(upload_to='channel/channel_cody')
	pub_date = models.DateTimeField('date published', default=datetime.now)

	objects = CodyManager()

	def __str__(self):
		return self.title

class CodyLikeManager(models.Manager):

		def get_or_create(self, user_id, cody_id):
			cody = Cody.objects.get(id=cody_id)
			user = User.objects.get(id=user_id)

			try:
				follow = CodyLike.objects.get(user=user_id, cody=cody_id)
			except:
				follow = CodyLike.objects.create(user=user_id, cody=cody_id)

			follow.whether_like = not follow.whether_like
			follow.save()

			return Cody.objects.filter(cody_likes_of_cody__user=user_id, cody_likes_of_cody__whether_like=True)

class CodyLike(models.Model):
	cody = models.ForeignKey(Cody, related_name='cody_likes_of_cody')
	user = models.ForeignKey(User, related_name='cody_likes_of_user')
	whether_like = models.BooleanField(default=False)

	objects = CodyLikeManager()

class CodyItem(models.Model):
	cody = models.ForeignKey(Cody, related_name='cody_items_of_cody')
	product = models.ForeignKey(Product, related_name='cody_items_of_product')
	tip = models.CharField(max_length=50)

	def __str__(self):
		return self.product.name + '(' + self.product.tag.gender.type + ')'

class LikeManager(models.Manager):

	def get_or_create(self, user, product):
		try:
			return Like.objects.get(user=user, product=product)
		except:
			return Like.objects.create(user=user, product=product)

	def like_count(self, product):
		return Like.objects.filter(product = product, whether_like = True).count()

class Like(models.Model):
	whether_like = models.BooleanField(default=False)
	product = models.ForeignKey(Product, related_name='likes_of_product')
	user = models.ForeignKey(User, related_name='likes_of_user')

	objects = LikeManager()


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
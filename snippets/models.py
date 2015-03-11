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
		try:
			category_list = Category.objects.filter(gender = gender_id)
			return category_list
		except:
			print("no one's category")
			return category_list

class Category(models.Model):
	gender = models.ForeignKey(Gender, related_name='categories_of_gender', blank=True, null=True)
	type = models.CharField(max_length=10, default='')

	objects = CategoryManager()

	def __str__(self):
		return self.gender.type + ' / ' + self.type

class TagManager(models.Manager):
	def get_tag_list(self, gender_id):
		try:
			tag_list = Tag.objects.filter(gender=gender_id)
			return tag_list
		except:
			print("exception in CategoryManager get_men_category")
			return []

class Tag(models.Model):
	gender = models.ForeignKey(Gender, related_name='tags_of_gender', blank=True, null=True)
	category = models.ForeignKey(Category, related_name='tags_of_category', blank=True, null=True)
	name = models.CharField(max_length=20, default='')

	objects = TagManager()

	def __str__(self):
		return self.name + '(' + self.gender.type + ')'

class DesignerManager(models.Manager):

	def get_without_follow(self, user_id, gender_id):

		follows_designer_id = []


		follows = DesignerFollow.objects.filter(user=user_id, whether_follow=True)

		for follow in follows:
				follows_designer_id.append(follow.designer.id)

		filtered_designer = Designer.objects.exclude(id__in=follows_designer_id).filter(gender=gender_id)

		return filtered_designer

class Designer(models.Model):
	user = models.OneToOneField(User)
	gender = models.ForeignKey(Gender, max_length=5, related_name='designers_of_gender', blank=True, null=True)
	name = models.CharField(max_length=20)
	intro = models.TextField(max_length=200, blank=True)
	image = models.ImageField(upload_to='upload/designer', default='')
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

		follows_of_user = Designer.objects.filter(designer_follows_of_designer__user=user_id, designer_follows_of_designer__whether_follow=True)

		return follows_of_user

class DesignerFollow(models.Model):
	user = models.ForeignKey(User, related_name="designer_follows_of_user")
	designer = models.ForeignKey(Designer, related_name="designer_follows_of_designer")
	whether_follow = models.BooleanField(default=False)

	objects = DesignerFollowManager()


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

	"""
	def get_without_follow(self, user_id):

		follows = Product.objects.filter(products_of_designer__designer_follows_of_designer = user_id, products_of_designer__designer_whether_follow = False).order_by('-created')
		return follows
	"""

class Product(models.Model):
	designer = models.ForeignKey(Designer, related_name='products_of_designer', blank=True, null=True)
	tag = models.ForeignKey(Tag, related_name='products_of_tag', blank=True, null=True)
	pub_date = models.DateTimeField('date published', default=datetime.now)
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=100)
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to='upload')

	objects = ProductManager()

	def __str__(self):
		return self.name

class AdminChannel(models.Model):
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='channel')

class ChannelManager(models.Manager):

	def get_without_follow(self, user_id):

		follows_channel_id = []

		try:
			follows = ChannelFollow.objects.filter(user=user_id, whether_follow=True)

			for follow in follows:
				follows_channel_id.append(follow.channel.id)

			filtered_channel = Channel.objects.exclude(id__in=follows_channel_id)
		# no one channel of following
		except:
			filtered_channel = Channel.objects.all()

		return filtered_channel

	def get_channel_of_cody(self, cody_id):

		channel = Channel.objects.get(codies_of_channel__id=cody_id)

		return channel

class Channel(models.Model):
	name = models.CharField(max_length=30)
	intro = models.TextField(max_length=200)
	image = models.ImageField(upload_to='channel')
	web = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	created = models.DateTimeField('date created', default=datetime.now)

	objects = ChannelManager()

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

		follows_of_user = Channel.objects.filter(channel_follows_of_channel__user=user_id, channel_follows_of_channel__whether_follow=True)

		return follows_of_user

class ChannelFollow(models.Model):
	channel = models.ForeignKey(Channel, related_name="channel_follows_of_channel")
	user = models.ForeignKey(User, related_name="channel_follows_of_user")
	whether_follow = models.BooleanField(default=False)

	objects = ChannelFollowManager()

class CodyManager(models.Manager):
	def get_without_follow(self, user_id):

		follows_channel_id = []

		try:
			follows = ChannelFollow.objects.filter(user=user_id, whether_follow=True)

			for follow in follows:
				follows_channel_id.append(follow.channel.id)

			filtered_cody = Cody.objects.exclude(channel_id__in=follows_channel_id)
		# no one channel of following
		except:
			filtered_cody = Cody.objects.all()

		return filtered_cody


class Cody(models.Model):
	channel = models.ForeignKey(Channel, related_name='codies_of_channel')
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

			print("cody", cody_id)
			print("user", user_id)

			try:
				follow = CodyLike.objects.get(user=user, cody=cody)
			except:
				print("cody like create")
				follow = CodyLike.objects.create(user=user, cody=cody)

			follow.whether_like = not follow.whether_like
			follow.save()

			follows_of_user = Cody.objects.filter(cody_likes_of_cody__user=user, cody_likes_of_cody__whether_like=True)

			return follows_of_user

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
		return self.product.name

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
	product = models.ForeignKey(Product, related_name='likes_of_product')
	user = models.ForeignKey(User, related_name='likes_of_user')

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

class CartItem(models.Model):
	product = models.ForeignKey(Product, related_name='cart_items_of_product')
	cart = models.ForeignKey(Cart, related_name='cart_items_of_cart')
	size = models.CharField(null=True, max_length=10)
	color = models.CharField(null=True, max_length=10)
	quantity = models.IntegerField(null=True)
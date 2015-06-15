from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import os

from second.settings import AUTH_USER_MODEL

class HashTagCategory(models.Model):
    name        = models.CharField(unique=True, max_length=10, blank=False)
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HashTagManager(models.Manager):
    def get_pop_hashtag(self):
        HashTag.objects.filter()

class HashTag(models.Model):
    name        = models.CharField(unique=True, max_length=10, blank=False)
    category    = models.ForeignKey(HashTagCategory, blank=False)

    objects     = HashTagManager()

    def __str__(self):
        if self.category.is_required == True:
            return '[' + self.category.name + ']' + self.name
        else:
            return self.name

    class Meta:
        ordering = ('category',)


class Gender(models.Model):
    type        = models.CharField(max_length=8)

    def __str__(self):
        return self.type

class BrandManager(models.Manager):
    def get_without_follow(self, user_id, gender_id):
        if user_id is not None:
            follow_brands = BrandFollow.objects.filter(user=user_id)

            return Brand.objects.exclude(brand_follows_of_brand__in=follow_brands).filter(gender=gender_id)
        else:  # anonymous user
            return Brand.objects.all()


class Brand(models.Model):
    designer    = models.OneToOneField(AUTH_USER_MODEL, verbose_name='디자이너', blank=False)
    gender      = models.ForeignKey(Gender, verbose_name='디자인 타겟', max_length=5, related_name='brands_of_gender', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True)
    profile     = models.ImageField(upload_to='upload/brand', default='')
    background  = models.ImageField(upload_to='upload/brand/background', default='')
    web         = models.URLField('웹 페이지', blank=True)
    address     = models.CharField('오프라인 주소', max_length=200, blank=True)

    objects     = BrandManager()

    def __str__(self):
        return self.name + '(' + self.gender.type + ')'


class BrandInterview(models.Model):
    brand       = models.ForeignKey(Brand, related_name='interviews')

    def get_upload_path(instance, filename):
        path = os.path.join("upload/brand/%s/interviews/" % instance.brand.name, filename)
        return path

    image       = models.ImageField(upload_to=get_upload_path)

class BrandFollowManager(models.Manager):
    def is_follow(self, user_id, brand_id):
        try:
            return BrandFollow.objects.get(user=user_id, brand=brand_id) is not None
        except:
            return False


class BrandFollow(models.Model):
    user        = models.ForeignKey(AUTH_USER_MODEL, related_name="brand_follows_of_user")
    brand       = models.ForeignKey(Brand, related_name="brand_follows_of_brand")

    objects     = BrandFollowManager()


class Product(models.Model):
    gender      = models.ForeignKey(Gender, blank=False, null=True)
    hash_tags   = models.ManyToManyField(HashTag, related_name='products', blank=False)
    brand       = models.ForeignKey(Brand, related_name='products_of_brand', blank=True, null=True)
    pub_date    = models.DateTimeField('date published', default=datetime.now, blank=True)
    name        = models.CharField(unique=True, max_length=15)
    description = models.TextField(max_length=100, default='')
    price       = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product     = models.ForeignKey(Product, related_name='images')
    description = models.TextField(max_length=1000, default='', blank=True)

    def get_upload_path(instance, filename):
        path = os.path.join("product/%s/" % instance.product.name, filename)
        return path

    image       = models.ImageField(upload_to=get_upload_path)

class Channel(models.Model):
    maker       = models.OneToOneField(AUTH_USER_MODEL, verbose_name="컨텐츠 제작자", blank=False)
    brief       = models.CharField(max_length=10, blank=False)
    created     = models.DateTimeField('date created', auto_now_add=True, blank=True)
    introduce   = models.TextField(max_length=200)

    def get_profile_path(instance, filename):
        path = os.path.join("channels/%s_profile_" % instance.maker, filename)
        return path

    def get_background_path(instance, filename):
        path = os.path.join("channels/%s_background_" % instance.maker, filename)
        return path

    profile     = models.ImageField(upload_to=get_profile_path)
    background  = models.ImageField(upload_to=get_background_path)

    def __str__(self):
        return self.name


class ChannelFollowManager(models.Manager):
    def is_follow(self, user_id, channel_id):
        try:
            return ChannelFollow.objects.get(user=user_id, channel=channel_id) is not None
        except:
            return False


class ChannelFollow(models.Model):
    user        = models.ForeignKey(AUTH_USER_MODEL, related_name="channel_follows_of_user")
    channel     = models.ForeignKey(Channel, related_name="channel_follows_of_channel")

    objects     = ChannelFollowManager()


class IssueManager(models.Manager):
    def get_without_follow(self, user_id):

        try:
            follow_channels = ChannelFollow.objects.filter(user=user_id).values_list('channel', flat=True)

            return Issue.objects.exclude(channel__in=follow_channels)
            # no one channel with following
        except:
            return Issue.objects.all()


class Issue(models.Model):
    pub_date    = models.DateTimeField('date published', default=datetime.now, blank=True)
    hash_tags   = models.ManyToManyField(HashTag, related_name='issues')
    channel     = models.ForeignKey(Channel, related_name='issues_of_channel')
    title       = models.CharField(unique=True, max_length=10)
    description = models.TextField(max_length=200, default='')
    image       = models.ImageField(upload_to='channel/channel_issue', default='')
    view        = models.PositiveIntegerField(default=0)

    objects     = IssueManager()

    def __str__(self):
        return self.title


class IssueLikeManager(models.Manager):
    def is_like(self, user_id, issue_id):
        try:
            return IssueLike.objects.get(user=user_id, issue=issue_id) is not None
        except:
            return False


class IssueLike(models.Model):
    issue       = models.ForeignKey(Issue, related_name='issue_likes_of_issue')
    user        = models.ForeignKey(AUTH_USER_MODEL, related_name='issue_likes_of_user')

    objects     = IssueLikeManager()


class IssueItem(models.Model):
    issue       = models.ForeignKey(Issue, related_name='issue_items_of_issue')
    product     = models.ForeignKey(Product, related_name='issue_items_of_product')
    tip         = models.CharField(max_length=50)


class ProductLikeManager(models.Manager):
    def is_like(self, user_id, product_id):
        try:
            return ProductLike.objects.get(user=user_id, product=product_id) is not None
        except:
            return False


class ProductLike(models.Model):
    product     = models.ForeignKey(Product, related_name='product_likes_of_product')
    user        = models.ForeignKey(AUTH_USER_MODEL, related_name='product_likes_of_user')

    objects     = ProductLikeManager()


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

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            nickname=nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

from django.core.validators import MinLengthValidator

class User(AbstractBaseUser):
    email       = models.EmailField('이메일 주소', max_length=255, unique=True, blank=False)
    nickname    = models.CharField('별명',     max_length=20, unique=True, blank=False, validators=[MinLengthValidator(4)])

    date_joined = models.DateTimeField('가입일', auto_now_add=True)

    is_active   = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)

    objects     = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.nickname

    def __str__(self):              # __unicode__ on Python 2
        return self.nickname

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
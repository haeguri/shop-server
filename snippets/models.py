from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import os

from second.settings import AUTH_USER_MODEL

class TestContent(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField()
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = TestContent.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(TestContent, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

class HashTagCategory(models.Model):
    name        = models.CharField(unique=True, max_length=10, blank=False)
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HashTag(models.Model):
    name        = models.CharField(unique=True, max_length=10, blank=False)
    category    = models.ForeignKey(HashTagCategory, blank=False)

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



class Product(models.Model):
    gender      = models.ForeignKey(Gender, blank=False, null=True)
    hash_tags   = models.ManyToManyField(HashTag, related_name='products', blank=False)
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

from django_summernote.models import Attachment
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import shutil

@receiver(pre_delete, sender=Attachment)
def attachment_delete(sender, instance, **kwargs):
    pass


@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    from second.settings import BASE_DIR

    shutil.rmtree(os.path.join('%s/media/product/' % BASE_DIR, instance.name))


@receiver(pre_delete, sender=ProductImage)
def product_image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete()

@receiver(pre_delete, sender=Channel)
def channel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete()
    instance.background.delete()


@receiver(pre_delete, sender=Issue)
def issue_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete()

@receiver(pre_delete, sender=TestContent)
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

    def exist_email(self, email):
        try:
            User.objects.get(email = email)
            return True
        except:
            return False




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
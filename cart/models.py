from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from snippets.models import Product

class CartManager(models.Manager):
	def check_and_create(self, user):
		try:
			Cart.objects.get(user = user)
		except:
			Cart.objects.create(user = user)

class CartInfo(models.Model):

	objects 	= CartManager()

	class Meta:
		abstract = True

class Cart(CartInfo):
	user 		= models.OneToOneField(User)

class Order(CartInfo):
	TYPE_OF_PAY	= (
		('mobile', '휴대폰'),
		('card', '신용카드'),
	)
	STATE_OF_SHIP = (
		('wait', '출고대기'),
		('outbound', '출고'),
		('delivery', '배송중'),
		('complete', '배송완료'),
	)
	STATE_OF_PAY = (
		('wait', '결제대기'),
		('complete', '결제완료'),
	)

	user 		= models.ForeignKey(User, related_name='orders_of_user')

	recipient 	= models.CharField('수령인', max_length=10, default='', blank=False)
	mobile_no	= models.CharField('모바일번호', max_length=15, default='', blank=False)
	addr1 		= models.CharField('주소1', max_length=100, default='', blank=False)
	addr2 		= models.CharField('주소2', max_length=100, default='', blank=False)
	ship_msg 	= models.TextField('배송메세지', max_length=500, default='', blank=False)
	means_pay	= models.CharField('결제수단', max_length=2, choices=TYPE_OF_PAY, default='mobile', blank=False)

	order_date 	= models.DateTimeField('주문일', default=timezone.localtime(timezone.now()))

	state_ship	= models.CharField('배송상태', max_length=20, choices=STATE_OF_SHIP, default='wait')
	state_pay	= models.CharField('결제상태', max_length=20, choices=STATE_OF_PAY, default='wait')

	sum_price	= models.PositiveIntegerField('구매가격', default=0, blank=True)
	shipping 	= models.PositiveIntegerField('배송료', default=2500, blank=True)
	total_price = models.PositiveIntegerField('합계금액', default=0, blank=True)

	def save(self, *args, **kwargs):
		items_of_order = self.items_of_cart

		self.sum_price = sum([item.product.price for item in items_of_order])

		if self.sum_price > 30000:
			self.shipping = 0

		self.total_price = self.shipping + self.sum_price
		super(Order, self).save(*args, **kwargs)


# CartItem 인스턴스들이 중복이 안되도록 막아야함.
class CartItem(models.Model):
	product 	= models.ForeignKey(Product, related_name='cart_items_of_product')
	cart 		= models.ForeignKey(Cart, related_name='cart_items_of_cart')

	size 		= models.CharField(max_length=10, null=True) # size 필드를 choices field로
	color 		= models.CharField(max_length=10, null=True)
	quantity 	= models.IntegerField(null=True)
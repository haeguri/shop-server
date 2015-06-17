from django.core.paginator import Paginator

from django.views.generic import ListView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from second.custom_auth import UserDetailsSerializer

from snippets.models import Product, ProductLike, Channel, HashTag,  \
	ChannelFollow, Issue, IssueLike, Brand, BrandFollow

from snippets.serializers import ProductSerializer, BrandSerializer, \
	ChannelSerializer, IssueSerializer, HashTagSerializer, \
	PaginationProductSerializer, PaginationIssueSerializer, \
	PaginationChannelSerializer

from django.contrib.auth import get_user_model


from second.middleware import UserTypeFilterMiddleware

User = get_user_model()

@api_view(['GET'])
def search_tag(request):

	keyword = request.QUERY_PARAMS.get('keyword')

	try:
		print ("keyword", keyword)
	except:
		pass

	hash_tags = HashTag.objects.filter(name__startswith=keyword)

	serializer = HashTagSerializer(hash_tags, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def hashtag_list(request):

	hash_tags = HashTag.objects.filter(category__name__in=['상품소분류', '성별']).reverse()[:5]

	serializer = HashTagSerializer(hash_tags, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def channel_list(request):

	page = request.QUERY_PARAMS.get('page')

	channels = Channel.objects.all()

	paginator = Paginator(channels, 6)
	channels = paginator.page(page)
	serializer = PaginationChannelSerializer(channels, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def channel_detail(request, channel_id):

	channel = Channel.objects.get(id=channel_id)
	serializer = ChannelSerializer(channel, many=False, context={'request':request})

	return Response(serializer.data	)


@api_view(['GET'])
def product_list(request):

	page, tag, brand = request.QUERY_PARAMS.get('page'), request.QUERY_PARAMS.get('tag'), request.QUERY_PARAMS.get('brand')

	if tag and page and brand:
		products = Product.objects.filter(hash_tags__id=tag, brand=brand)
	elif tag and page:
		products = Product.objects.filter(hash_tags__id=tag)
	elif page and brand:
		products = Product.objects.filter(brand=brand)
	elif page:
		products = Product.objects.all()

	paginator = Paginator(products, 6)
	products = paginator.page(page)
	serializer = PaginationProductSerializer(products, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request, product_id):

	product = Product.objects.get(id=product_id)
	serializer = ProductSerializer(product, many=False, context={'request':request})

	return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def issue_list(request):

	page, channel, tag = request.QUERY_PARAMS.get('page'), request.QUERY_PARAMS.get('channel'), request.QUERY_PARAMS.get('tag')

	if channel and tag and page:
		issues = Issue.objects.filter(hash_tags__id=tag, channel__id=channel)
	elif tag and page :
		issues = Issue.objects.filter(hash_tags__id=tag)
	elif page:
		issues = Issue.objects.all()

	paginator = Paginator(issues, 6)
	paged_issues = paginator.page(page)
	serializer = PaginationIssueSerializer(paged_issues, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def issue_detail(request, issue_id):

	issue = Issue.objects.get(id=issue_id)
	issue.view += 1
	issue.save()

	serializer = IssueSerializer(issue, many=False, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def brand_detail(request, brand_id):

	brand = Brand.objects.get(id=brand_id)

	serializer = BrandSerializer(brand, many=False, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def brand_products(request, brand_id):

	product_id = request.QUERY_PARAMS.get('product_id')

	if request.method == 'GET' and product_id is not None:
		rel_products = Product.objects.filter(brand=brand_id).exclude(id=product_id)
		serializer = ProductSerializer(rel_products, many=True)

	return Response(serializer.data, status.HTTP_200_OK)


from django.utils.decorators import decorator_from_middleware


@decorator_from_middleware(UserTypeFilterMiddleware)
@api_view(['GET'])
def user_detail(request, user_id):

	user = User.objects.get(id=user_id)
	#Cart.objects.check_and_create(user)

	# from post_office import mail
    #
	# mail.send(
	# 	['maphisto1@naver.com'],
	# 	'haegyun821@gmail.com',
	# 	subject='My email',
	# 	message='Hi there!',
	# 	html_message='Hi <strong>there</strong>!',
	# 	priority='now',
	# )

	# test = mail.send(
	# 	'maphisto1@naver.com', # List of email addresses also accepted
	# 	'haegyun821@gmail.com',
	# 	subject='My email',
	# 	message='Hi there!',
	# 	html_message='Hi <strong>there</strong>!',
	# )

	if request.method == 'GET':
		serializer = UserDetailsSerializer(user, many=False, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', 'DELETE'])
def product_like(request, user_id, product_id):
	user = User.objects.get(id=user_id)
	product = Product.objects.get(id=product_id)
	product_likes = ProductLike.objects.filter(user=user, product=product)

	if request.method == 'POST':
		if len(product_likes):
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			ProductLike.objects.create(user=user, product=product)
			return Response(status=status.HTTP_201_CREATED)

	elif request.method == 'DELETE':
		product_likes.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def issue_like(request, user_id, issue_id):
	user = User.objects.get(id=user_id)
	issue = Issue.objects.get(id=issue_id)
	issue_likes = IssueLike.objects.filter(user=user, issue=issue)

	if request.method == 'POST':
		if len(issue_likes) != 0:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			IssueLike.objects.create(user=user, issue=issue)
			return Response(status=status.HTTP_201_CREATED)

	elif request.method == 'DELETE':
		issue_likes.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def brand_follow(request, user_id, brand_id):
	user = User.objects.get(id=user_id)
	brand = Brand.objects.get(id=brand_id)
	brand_follows = BrandFollow.objects.filter(user=user, brand=brand)

	if request.method == 'POST':
		if len(brand_follows) != 0:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			BrandFollow.objects.create(user=user, brand=brand)
			return Response(status=status.HTTP_201_CREATED)

	elif request.method == 'DELETE':
		brand_follows.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def channel_follow(request, user_id, channel_id):
	user = User.objects.get(id=user_id)
	channel = Channel.objects.get(id=channel_id)
	channel_follows = ChannelFollow.objects.filter(user=user, channel=channel)

	if request.method == 'POST':
		if len(channel_follows) != 0:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		else:
			ChannelFollow.objects.create(user=user, channel=channel)
			return Response(status=status.HTTP_201_CREATED)

	elif request.method == 'DELETE':
		channel_follows.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

from django.contrib.auth.views import password_reset_confirm

def ladio_password_reset_confirm(request, uidb64=None, token=None):
	# return password_reset_confirm(request, uidb64=uidb36, token=token,
	# 							template_name='auth/password_reset_confirm.html')
	return password_reset_confirm(request, template_name='auth/password_reset_confirm.html',
		uidb64=uidb64, token=token)



from rest_auth.views import PasswordReset
from rest_auth.views import PasswordChange

class LadioPasswordReset(PasswordReset):
	def post(self, request, *args, **kwargs):
		email = request.DATA.get("email")
		try:
			# 소셜 계정으로 로그인한 사용자인가?
			User.objects.get(email=email, socialaccount__isnull=True)
		except:
			# 그렇다면 패스워드 찾기 기능은 이용할 수 없다.
			return Response({"social user"}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=request.DATA)

		if not serializer.is_valid():
			return Response(serializer.errors,
								status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response({"success": "Password reset e-mail has been sent."},
								status=status.HTTP_200_OK)

class LadioPasswordChange(PasswordChange):

	def post(self, request):
		try:
			# 소셜 계정으로 로그인한 사용자인가?
			User.objects.get(id=request.user.id, socialaccount__isnull=True)
		except:
			# 그렇다면 패스워드 변경 기능은 이용할 수 없다.
			return Response({"social user"}, status=status.HTTP_400_BAD_REQUEST)

		serializer = self.get_serializer(data=request.DATA)
		if not serializer.is_valid():
			return Response(serializer.errors,
				status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response({"success": "New password has been saved."})

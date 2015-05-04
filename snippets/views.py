from django.contrib.auth.models import User
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from second.custom_auth import CustomUserDetailsSerializer

from snippets.models import Product, ProductLike, Channel, HashTag,  \
	ChannelFollow, Issue, IssueLike, Brand, BrandFollow, BrandFeed, PubDay

from snippets.serializers import ProductSerializer, BrandSerializer, \
	ChannelSerializer, IssueSerializer, HashTagSerializer, \
	PaginationProductSerializer, PaginationIssueSerializer, \
	PaginationChannelSerializer, BrandFeedSerializer, PaginationBrandFeedSerializer, \
	PubDaySerializer

from cart.serializer import Cart

@api_view(['GET'])
def search_tag(request):

	keyword = request.QUERY_PARAMS.get('keyword')

	hash_tags = HashTag.objects.filter(name__startswith=keyword)

	serializer = HashTagSerializer(hash_tags, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def hashtag_list(request):

	hash_tags = HashTag.objects.filter(category__name__in=['상품소분류', '성별']).reverse()[:5]

	serializer = HashTagSerializer(hash_tags, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def pubday_list(request):

	pub_days = PubDay.objects.all()

	serializer = PubDaySerializer(pub_days, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def channel_list(request):

	page, day = request.QUERY_PARAMS.get('page'), request.QUERY_PARAMS.get('day')

	query_test = request.QUERY_PARAMS.get('query')

	print("query_test", query_test)

	if page and day in ['월', '화', '수', '목', '금', '토']:
		channels = Channel.objects.filter(pub_days__day=day)
	else:
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
def feed_list(request):

	page, brand = request.QUERY_PARAMS.get('page'), request.QUERY_PARAMS.get('brand')

	if page and brand:
		feeds = BrandFeed.objects.filter(brand=brand)

		paginator = Paginator(feeds, 3)
		paged_feeds = paginator.page(page)
		serializer = PaginationBrandFeedSerializer(paged_feeds, context={'request':request})

	elif page:

		user = request.user
		feeds = BrandFeed.objects.filter(brand__brand_follows_of_brand__user=user)

		paginator = Paginator(feeds, 3)
		paged_feeds = paginator.page(page)
		serializer = PaginationBrandFeedSerializer(paged_feeds, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)


"""
@api_view(['GET'])
def product_list(request):

	page = request.QUERY_PARAMS.get('page')
	filter = request.QUERY_PARAMS.get('filter')

	if page is not None:
		paginator = Paginator(queryset, 6)

		products = paginator.page(page)

		serializer = PaginatedProductSerializer(products, context={'request':request})

	elif filter == 'brand':
		products = Product.objects.filter(brand=request.QUERY_PARAMS.get('brand_id'))[:4]
		serializer = ProductSerializer(products, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request, gender_id, tag_id, product_id):

	if request.method == 'GET':
		product = Product.objects.get(id=product_id)
		serializer = ProductSerializer(product, many=False, context={'request':request})

	return Response(serializer.data)

@api_view(['GET'])
def brand_list(request, gender_id):

	if request.method == 'GET':
		brands = Brand.objects.get_without_follow(request.user.id, gender_id)
		serializer = BrandSerializer(brands, many=True, context={'request':request})

		return Response(serializer.data)


@api_view(['GET', 'POST'])
def brand_detail(request, gender_id, brand_id):

	if request.method == 'GET':
		brand = Brand.objects.get(id=brand_id)
		serializer = BrandSerializer(brand, many=False, context={'request':request})

		return Response(serializer.data, status.HTTP_200_OK)


"""

@api_view(['GET'])
def brand_products(request, brand_id):

	product_id = request.QUERY_PARAMS.get('product_id')

	if request.method == 'GET' and product_id is not None:
		rel_products = Product.objects.filter(brand=brand_id).exclude(id=product_id)
		serializer = ProductSerializer(rel_products, many=True)

	return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def user_detail(request, user_id):
	try:
		user = User.objects.get(id=user_id)
		cart = Cart.objects.get_or_create(user.id)
	except User.DoesNotexist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CustomUserDetailsSerializer(user, many=False, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', 'DELETE'])
def product_like(request, user_id, product_id):
	user = User.objects.get(id=user_id)
	product = Product.objects.get(id=product_id)

	if request.method == 'POST':
		try:
			ProductLike.objects.create(user=user, product=product)
			return Response(status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		product_like = ProductLike.objects.get(user=user, product=product)
		product_like.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def issue_like(request, user_id, issue_id):
	user = User.objects.get(id=user_id)
	issue = Issue.objects.get(id=issue_id)

	if request.method == 'POST':
		try:
			IssueLike.objects.create(user=user, issue=issue)
			return Response(status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		issue_like = IssueLike.objects.get(user=user, issue=issue)
		issue_like.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def brand_follow(request, user_id, brand_id):
	user = User.objects.get(id=user_id)
	brand = Brand.objects.get(id=brand_id)
	if request.method == 'POST':
		try:
			BrandFollow.objects.create(user=user, brand=brand)
			return Response(status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		brand_follow = BrandFollow.objects.get(user=user, brand=brand)
		brand_follow.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'DELETE'])
def channel_follow(request, user_id, channel_id):
	user = User.objects.get(id=user_id)
	channel = Channel.objects.get(id=channel_id)

	if request.method == 'POST':
		try:
			print("before")
			ChannelFollow.objects.create(user=user, channel=channel)
			print("after")
			return Response(status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		channel_follow = ChannelFollow.objects.get(user=user, channel=channel)
		channel_follow.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
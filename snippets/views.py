from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.views.generic import ListView

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

from cart.models import Cart

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
def pubday_list(request):

	pub_days = PubDay.objects.all()

	serializer = PubDaySerializer(pub_days, many=True, context={'request':request})

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def channel_list(request):

	page, day = request.QUERY_PARAMS.get('page'), request.QUERY_PARAMS.get('day')

	query_test = request.QUERY_PARAMS.get('query')

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

@api_view(['GET'])
def brand_products(request, brand_id):

	product_id = request.QUERY_PARAMS.get('product_id')

	if request.method == 'GET' and product_id is not None:
		rel_products = Product.objects.filter(brand=brand_id).exclude(id=product_id)
		serializer = ProductSerializer(rel_products, many=True)

	return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def user_detail(request, user_id):

	user = User.objects.get(id=user_id)
	#Cart.objects.check_and_create(user)

	if request.method == 'GET':
		serializer = CustomUserDetailsSerializer(user, many=False, context={'request':request})

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
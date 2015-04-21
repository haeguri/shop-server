from django.contrib.auth.models import User
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from second.custom_auth import CustomUserDetailsSerializer

from snippets.models import Product, ProductLike, Channel, \
	ChannelFollow, Issue, IssueLike, Brand, BrandFollow, ProductSort

from snippets.serializers import ProductSerializer, BrandSerializer, \
	ChannelSerializer, IssueSerializer, PaginatedProductSerializer, GenderSerializer, \
	ProductSortSerializer

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
def issue_list(request):

	if request.method == 'GET':

		if request.QUERY_PARAMS.get('reco') == 'shuffle':
			import random
			issue_list = list(Issue.objects.all())
			random.shuffle(issue_list)
			issue_list = issue_list[0:4]
		else:
			issue_list = Issue.objects.all()

		serializer = IssueSerializer(issue_list, many=True, context={'request':request},
														  fields=('id', 'channel', 'title', 'image', 'pub_date'))


		return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET','POST'])
def channel_detail(request, channel_id):

	if request.method == 'GET':
		channel = Channel.objects.get(id=channel_id)
		serializer = ChannelSerializer(channel, many=False, context={'request':request})

		return Response(serializer.data	)

@api_view(['GET', 'POST'])
def issue_detail(request, channel_id, issue_id):

	if request.method == 'GET':
		issue = Issue.objects.get(id=issue_id)
		serializer = IssueSerializer(Issue, many=False, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_detail(request, user_id):
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotexist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CustomUserDetailsSerializer(user, many=False, context={'request':request})

		return Response(serializer.data)

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
			ChannelFollow.objects.create(user=user, channel=channel)
			return Response(status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		channel_follow = ChannelFollow.objects.get(user=user, channel=channel)
		channel_follow.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Gender, Product, Like, Category, Cart, CartItem, Channel, ChannelFollow, \
	Cody, CodyItem, CodyLike, Tag, Designer, DesignerFollow
from snippets.serializers import ProductSerializer, UserSerializer, CategorySerializer, TagSerializer, \
	CartReadSerializer, CartWriteSerializer, ItemWriteSerializer, ItemReadSerializer, DesignerSerializer, \
	ChannelSerializer, CodySerializer, CodyItemSerializer, PaginatedProductSerializer, GenderSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.paginator import Paginator

import json

@api_view(['GET'])
def gender_list(request):
	if request.method == 'GET':
		genders = Gender.objects.all().order_by('-type')
		serializer = GenderSerializer(genders, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_list(request, gender_id):
	if request.method == 'GET':
		categories = Category.objects.get_category_list(gender_id)
		serializer = CategorySerializer(categories, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def tag_list(request, gender_id):
	filter = request.QUERY_PARAMS.get('filter')

	if request.method == 'GET':

		tags = Tag.objects.get_tags(gender_id)
		serializer = TagSerializer(tags, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_list(request):

	tag_id = request.QUERY_PARAMS.get('tag_id')
	queryset = Product.objects.filter(tag=tag_id).order_by('-pub_date')
	paginator = Paginator(queryset, 6)

	page = request.QUERY_PARAMS.get('page')

	try:
		products = paginator.page(page)
	except:
		print("pagination error")

	serializer = PaginatedProductSerializer(products)

	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request, product_id):
	follow = request.QUERY_PARAMS.get('designer')

	if request.method == 'GET':
		product = Product.objects.get(id=product_id)
		serializer = ProductSerializer(product)

		return Response(serializer.data)

@api_view(['GET', 'POST'])
def category_cody_list(request, category_id):

	if request.method == 'GET':
		codies = Cody.objects.get_codies_of_category(category_id)
		serializer = CodySerializer(codies, many=True)

		return Response(serializer.data)

@api_view(['GET','POST'])
def channel_detail(request, channel_id):
	user_id = request.QUERY_PARAMS.get('user_id')

	if request.method == 'GET':
		channel = Channel.objects.get(id=channel_id)
		serializer = ChannelSerializer(channel, many=False)

		return Response(serializer.data	)

	elif request.method == 'POST':

		follows_of_user = ChannelFollow.objects.get_or_create(user_id, channel_id)

		serializer = ChannelSerializer(follows_of_user, many=True)

		return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def category_cody_list(request, category_id):

	if request.method == 'GET':
		codies = Cody.objects.get_codies_of_category(category_id).order_by('-pub_date')
		serializer = CodySerializer(codies, many=True);

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def cody_list(request, channel_id):

	if request.method == 'GET':
		codies = Cody.objects.filter(channel=channel_id)
		serializer = CodySerializer(codies, many=True)

		return Response(serializer.data)

@api_view(['GET', 'POST'])
def cody_detail(request, channel_id, cody_id):
	user_id = request.QUERY_PARAMS.get('user_id')

	if request.method == 'GET':
		cody = Cody.objects.get(id=cody_id)
		serializer = CodySerializer(cody, many=False)

		return Response(serializer.data, status=status.HTTP_200_OK)

	if request.method == 'POST':
		follows = CodyLike.objects.get_or_create(user_id, cody_id)
		serializer = CodySerializer(follows, many=True)

		return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def designer_list(request):
	user_id = request.QUERY_PARAMS.get('user_id')
	gender_id = request.QUERY_PARAMS.get('gender_id')

	if request.method == 'GET':
		designers = Designer.objects.get_without_follow(user_id, gender_id)
		serializer = DesignerSerializer(designers, many=True)

		return Response(serializer.data)

@api_view(['GET', 'POST'])
def designer_detail(request, designer_id):
	user_id = request.QUERY_PARAMS.get('user_id')

	if request.method == 'POST':
		follows = DesignerFollow.objects.get_or_create(user_id, designer_id)
		serializer = DesignerSerializer(follows, many=True)

		return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
def cart_list(request):

	if request.method == 'GET':

		try:
			cart = Cart.objects.get(user=request.QUERY_PARAMS.get('user_id'))
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = CartReadSerializer(cart, many=False)

			return Response(serializer.data)

	elif request.method == 'POST':

		if request.method == 'POST':
			serializer = ItemWriteSerializer(data=request.data)

			if serializer.is_valid():
				item = serializer.save()

				serializer = ItemReadSerializer(item, many=False)
				return Response(serializer.data, status=status.HTTP_201_CREATED)

			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		try:
			items = CartItem.objects.filter(id__in=request.data['del_list'])
			cart = Cart.objects.get_or_create(request.QUERY_PARAMS.get('user_id'))
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		items.delete()
		items = cart.cart_items_of_cart.all()
		serializer = ItemReadSerializer(items, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_data(request, user_id):
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotexist:
		print("exception")
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)

		return Response(serializer.data)

@csrf_exempt
def product_like(request, user_id, product_id):

	user = User.objects.get(id=user_id)
	product = Product.objects.get(id=product_id)

	if request.method == 'POST':
		try:
			like = Like.objects.get_or_create(user, product)
			like.whether_like = not like.whether_like
			like.save()

			response_data = {
				'likes': Like.objects.like_count(product),
				'status': Like.objects.get_or_create(user,product).whether_like,
			}

			return HttpResponse(json.dumps(response_data), content_type="application/json")
		except:
			print("exception!!!!!")
			pass

@api_view(['GET'])
def channel_follow_list(request):
	user_id = request.QUERY_PARAMS.get('user_id')
	channel_id = request.QUERY_PARAMS.get('channel_id')

	follow_channels = ChannelFollow.objects.get_or_create(user_id, channel_id)

	serializer = ChannelSerializer(follow_channels, many=True)

	return Response(serializer.data, status=status.HTTP_201_CREATED)
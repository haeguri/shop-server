from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import *
from snippets.serializers import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator

@api_view(['GET'])
def gender_list(request):
	if request.method == 'GET':
		genders = Gender.objects.all().order_by('-type')
		serializer = GenderSerializer(genders, many=True, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def tag_list(request, gender_id):
	filter = request.QUERY_PARAMS.get('filter')
	brand_id = request.QUERY_PARAMS.get('brand_id')

	if request.method == 'GET':
		if filter == 'brand':
			tags = Tag.objects.get_tags_of_brand(brand_id)
			serializer = TagSerializer(tags, many=True, context={'request':request})
			return Response(serializer.data, status=status.HTTP_200_OK)

		else:
			tags = Tag.objects.get_tags(gender_id)
			serializer = TagSerializer(tags, many=True, context={'request':request})
			return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_list(request, gender_id, tag_id):

	if 'page' not in request.QUERY_PARAMS:
		products = Product.objects.filter(tag=tag_id).order_by('-pub_date')

		serializer = ProductSerializer(products, many=True, context={'request':request})
	else:
		if tag_id is not None:
			queryset = Product.objects.filter(tag=tag_id).order_by('-pub_date')

		paginator = Paginator(queryset, 6)
		page = request.QUERY_PARAMS.get('page')

		try:
			products = paginator.page(page)
		except:
			print("pagination error")

		serializer = PaginatedProductSerializer(products, context={'request':request})

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
def brand_detail(request, brand_id):

	if request.method == 'GET':
		brand = Brand.objects.get(id=brand_id)
		serializer = BrandSerializer(brand, many=False, context={'request':request})

		return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def cody_list(request):

	if request.method == 'GET':
		cody_list = Cody.objects.all()
		serializer = CodySerializer(cody_list, many=True, context={'request':request},
														  fields=('id', 'channel', 'title', 'image', 'pub_date'))

		return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET','POST'])
def channel_detail(request, channel_id):

	if request.method == 'GET':
		channel = Channel.objects.get(id=channel_id)
		serializer = ChannelSerializer(channel, many=False, context={'request':request})

		return Response(serializer.data	)

@api_view(['GET', 'POST'])
def category_cody_list(request, category_id):

	if request.method == 'GET':
		codies = Cody.objects.get_codies_of_category(category_id).order_by('-pub_date')
		serializer = CodySerializer(codies, many=True, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def cody_detail(request, channel_id, cody_id):

	if request.method == 'GET':
		cody = Cody.objects.get(id=cody_id)
		serializer = CodySerializer(cody, many=False, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_detail(request, user_id):
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotexist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user, many=False, context={'request':request})

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
def cody_like(request, user_id, cody_id):
	user = User.objects.get(id=user_id)
	cody = Cody.objects.get(id=cody_id)

	if request.method == 'POST':
		try:
			CodyLike.objects.create(user=user, cody=cody)
			return Response(status=status.HTTP_201_CREATED)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		cody_like = CodyLike.objects.get(user=user, cody=cody)
		cody_like.delete()

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

@api_view(['GET', 'POST', 'DELETE'])
def cart_list(request):

	if request.method == 'GET':

		try:
			cart = Cart.objects.get(user=request.QUERY_PARAMS.get('user_id'))
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if request.method == 'GET':
			serializer = CartReadSerializer(cart, many=False, context={'request':request})

			return Response(serializer.data)

	elif request.method == 'POST':

		if request.method == 'POST':
			serializer = ItemWriteSerializer(data=request.data)

			if serializer.is_valid():
				item = serializer.save()

				serializer = ItemReadSerializer(item, many=False, context={'request':request})
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
		serializer = ItemReadSerializer(items, many=True, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

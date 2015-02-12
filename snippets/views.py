from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Product, Like, Category, Cart, CartItem
from snippets.serializers import ProductSerializer, UserSerializer, CategorySerializer, \
	CartReadSerializer, CartWriteSerializer, ItemWriteSerializer, ItemReadSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json

@api_view(['GET'])
def product_list(request, user_id):

	if request.method == 'GET':
		products = Product.objects.all().order_by('-pub_date')
		serializer = ProductSerializer(products, many=True)
		like_id_list = Product.objects.init_like(user_id)

		return Response(dict(items = serializer.data, like_items = like_id_list))

@api_view(['GET'])
def product_detail(request, user_id, product_id):
	if request.method == 'GET':
		product = Product.objects.get(id=product_id)
		serializer = ProductSerializer(product)

		return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
	if request.method == 'GET':
		men = Category.objects.get_men_category()
		women = Category.objects.get_women_category()
		men_serializer = CategorySerializer(men, many=True)
		women_serializer = CategorySerializer(women, many=True)

		return Response(dict(men = men_serializer.data, women = women_serializer.data))


@api_view(['GET', 'POST'])
def cart_view(request, user_id):

	try:
		cart = Cart.objects.get(user__id=user_id)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CartReadSerializer(cart, many=False)

		return Response(serializer.data)


@api_view(['POST', 'DELETE'])
def item_of_cart(request, user_id):

	if request.method == 'POST':
		serializer = ItemWriteSerializer(data=request.data)

		if serializer.is_valid():
			item = serializer.save()

			serializer = ItemReadSerializer(item, many=False)
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		try:
			items = CartItem.objects.filter(id__in=request.data['del_list'])
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		items.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)






@api_view(['GET', 'POST'])
def cart_init(request, user_id):
	if request.method == 'GET':
		cart = Cart.objects.get_or_create(user_id)
		serializer = CartReadSerializer(cart, many=False)

		return Response(serializer.data)


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
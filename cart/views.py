from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cart.models import Cart, CartItem
from cart.serializer import ItemWriteSerializer, ItemReadSerializer, CartReadSerializer
from django.contrib.auth.models import User

@api_view(['GET', 'POST', 'DELETE'])
def cart_detail(request):

	if request.method == 'GET':

		cart = Cart.objects.get_or_create(request.user.id)
		serializer = CartReadSerializer(cart, many=False, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def cart_item_list(request):
	if request.method == 'POST':
		print("resquerst.data", request.data)
		serializer = ItemWriteSerializer(data=request.data)

		if serializer.is_valid():
			item = serializer.save()

			serializer = ItemReadSerializer(item, many=False, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def cart_item_detail(request, item_id):
	if request.method == 'DELETE':
		try:
			#items = CartItem.objects.filter(id__in=request.data['del_list'])
			item = CartItem.objects.get(id=item_id)
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		item.delete()
		cart = Cart.objects.get(user=request.user)
		serializer = CartReadSerializer(cart, many=False, context={'request':request})
		#serializer = ItemReadSerializer(items, many=True, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def order(request):
	user = User.objects.get(request.user.id)

	pass
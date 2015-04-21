from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cart.models import Cart, CartItem
from cart.serializer import ItemWriteSerializer, ItemReadSerializer

@api_view(['GET', 'POST', 'DELETE'])
def cart_detail(request):

	if request.method == 'GET':

		try:
			cart = Cart.objects.get(user=request.QUERY_PARAMS.get('user_id'))
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE'])
def cart_item_list(request, user_id):
	if request.method == 'POST':
		serializer = ItemWriteSerializer(data=request.data)

		if serializer.is_valid():
			item = serializer.save()

			serializer = ItemReadSerializer(item, many=False, context={'request':request})
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def cart_item_detail(request, user_id, cart_item_id):
	if request.method == 'DELETE':
		try:
			items = CartItem.objects.filter(id__in=request.data['del_list'])
			cart = Cart.objects.get_or_create(request.QUERY_PARAMS.get('user_id'))
		except:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		items.delete()
		items = cart.cart_items_of_cart.all()
		serializer = ItemReadSerializer(items, many=True, context={'request':request})

		return Response(serializer.data, status=status.HTTP_200_OK)
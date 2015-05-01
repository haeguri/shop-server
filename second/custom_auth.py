from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_auth.serializers import TokenSerializer

from snippets.serializers import ProductLikeSerializer, ChannelFollowSerializer, BrandFollowSerializer, IssueLikeSerializer

from cart.serializer import CartReadSerializer

from cart.models import Cart

class CustomUserDetailsSerializer(serializers.ModelSerializer):

	product_likes_of_user = ProductLikeSerializer(many=True, fields=('id', 'product',))
	channel_follows_of_user = ChannelFollowSerializer(many=True, fields=('id', 'channel',))
	brand_follows_of_user = BrandFollowSerializer(many=True, fields=('id', 'brand',))
	issue_likes_of_user = IssueLikeSerializer(many=True, fields=('id', 'issue',))
	#cart = CartReadSerializer(many=False)
	cart = CartReadSerializer(many=False)

	class Meta:
		model = User
		fields = ('id', 'username','email', 'cart', 'product_likes_of_user', 'issue_likes_of_user', 'channel_follows_of_user', 'brand_follows_of_user',)

# When the login request is authenticated successfully, Default "TokenSerializer" has serializes the response data.
# "MyTokenSerializer" is the custom serializer instead of "TokenSerializer".
class CustomTokenSerializer(TokenSerializer):

    class Meta:
        model =  Token
        # Added the 'user' field
        fields = ('key','user')
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_auth.serializers import TokenSerializer

from snippets.serializers import ProductLikeSerializer, ChannelFollowSerializer, BrandFollowSerializer, IssueLikeSerializer

from cart.serializer import CartReadSerializer

class CustomUserDetailsSerializer(serializers.ModelSerializer):

	product_likes_of_user = ProductLikeSerializer(many=True, fields=('id', 'product',))
	channel_follows_of_user = ChannelFollowSerializer(many=True, fields=('id', 'channel',))
	brand_follows_of_user = BrandFollowSerializer(many=True, fields=('id', 'brand',))
	issue_likes_of_user = IssueLikeSerializer(many=True, fields=('id', 'issue',))
	#cart = CartReadSerializer(many=False)
	#cart = CartReadSerializer(many=False)

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'product_likes_of_user', 'issue_likes_of_user', 'channel_follows_of_user', 'brand_follows_of_user',)

# 로그인 요청이 성공적으로 처리되면 "TokenSerializer"가 "Token"을 직렬화해 response data로 보낸다.
# "TokenSerializer"를 상속받아 fields 속성에 'user' 필드를 추가한 "CustomTokenSerializer"를 기본 "TokenSerializer"로 사용하기로 했다.
class CustomTokenSerializer(TokenSerializer):

    class Meta:
        model =  Token
        # Added the 'user' field
        fields = ('key','user')
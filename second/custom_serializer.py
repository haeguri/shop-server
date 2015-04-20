from rest_framework import serializers
from rest_framework.authtoken.models import Token
from snippets.serializers import UserSerializer

from rest_auth.serializers import TokenSerializer

# When the login request is authenticated successfully, Default "TokenSerializer" has serializes the response data.
# "MyTokenSerializer" is the custom serializer instead of "TokenSerializer".
class MyTokenSerializer(TokenSerializer):

    class Meta:
        model =  Token
        # Added the 'user' field
        fields = ('key','user')
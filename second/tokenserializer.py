from rest_framework import serializers
from rest_framework.authtoken.models import Token
from snippets.serializers import UserSerializer

class CustomToken(Token):
    pass


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CustomToken
        fields = ('key','user')
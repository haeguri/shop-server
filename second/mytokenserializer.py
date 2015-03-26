from rest_framework import serializers
from rest_framework.authtoken.models import Token

class MyTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Token
        fields = ('key','user')
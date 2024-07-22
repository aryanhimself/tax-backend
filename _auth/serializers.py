from rest_framework import serializers
from users.models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_null=False)
    password = serializers.CharField(required=True, allow_null=False)

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['role']

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

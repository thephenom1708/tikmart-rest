from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import password_validation

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'mobile', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['first_name'],
                                        validated_data['last_name'], validated_data['password'])

        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials! Please try again!")


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirmed_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data.get('old_password')):
            raise serializers.ValidationError({'old_password': 'Incorrect current password'})

        if data.get('confirmed_password') != data.get('new_password'):
            raise serializers.ValidationError({'confirmed_password': 'Confirm Password does not match with new password'})

        password_validation.validate_password(data['new_password'], user)
        return data


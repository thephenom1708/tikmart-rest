from knox.models import AuthToken
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer, ChangePasswordSerializer


# Register API

class RegisterAPI(generics.CreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class ChangePasswordAPI(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({
            'success': True,
        }, status=status.HTTP_200_OK)


# Get User API
class UserAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        mobile = request.data.get('mobile')

        print(first_name, last_name, mobile)

        user.first_name = first_name
        user.last_name = last_name
        user.mobile = mobile
        user.save()

        return Response({
            "success": False
        }, status=status.HTTP_200_OK)

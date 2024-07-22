from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from utils import response

from users.models import User
from users.serializers import UserSerializer
from rest_framework import status 
from _auth.serializers import LoginSerializer, SignupSerializer

from django.middleware.csrf import get_token
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class AuthViewSet(viewsets.ViewSet):
    """
    User Login, Logout, Signup View Sets
    """
    authentication_classes = [SessionAuthentication]

    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        user = authenticate(request, email=data['email'], password=data['password'])
        if user == None:
            return Response('Invalid Credentials',status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        csrf_token = get_token(request)
        response_data = {
            'user': UserSerializer(user).data,
            'token': token.key,
            'csrf_token': csrf_token
        }
        response = Response(response_data)
        response.set_cookie('csrftoken', csrf_token, httponly=False,secure=False,domain=None,path='/', samesite='Lax')
        
        return response
        

    def logout(self, request):
        logout(request)
        return response.success('successfully logged out')


    def signup(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(request.data['password'])
            serializer.save()
            return response.success('user successfully registered', serializer.data)
        
        return response.bad_request(serializer.errors, {})

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        print(user)
        serializer = UserSerializer(instance=request.user, data={
            "first_name": user.first_name,
            "last_name": user.last_name ,
            "email": user.email,
            "phone": user.phone,
            "pan": user.pan,
            "maritial_status": user.maritial_status,
            "reward_points": user.reward_points + 1
        })
        if serializer.is_valid():
            serializer.save()
            return response.success('', serializer.data)
        return response.auth_required('', meta=serializer.errors)


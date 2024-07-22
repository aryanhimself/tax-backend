from rest_framework import viewsets, generics


from django.db.models import Q


from utils import response

from users.serializers import UserCreateSerializer, UserUpdateSerializer, UserSerializer
from users.models import User

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    page_size_query_param = 'limit'


    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        return User.objects.filter(
            Q(first_name__contains=q) |
            Q(last_name__contains=q) |
            Q(middle_name__contains=q) |
            Q(email__contains=q) |
            Q(phone__contains=q) |
            Q(pan__contains=q)
        ).order_by('-id')


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('user created', serializer.data)

        return response.bad_request(serializer.errors)

    def update(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return response.not_found('user not found')
        serializer = UserUpdateSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            return response.success('user updated', serializer.data)

        return response.bad_request(serializer.errors)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return response.not_found('user not found')
        serializer = UserSerializer(instance=user)
        return response.success('', serializer.data)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return response.not_found('user not found')
        user.delete()
        return response.success('', {})


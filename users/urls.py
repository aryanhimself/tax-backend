from django.urls import path

from users.views import UserViewSet, UserListAPIView

urlpatterns = [
    path('', UserViewSet.as_view({'post': 'create'})),
    path('list/', UserListAPIView.as_view()),
    path('<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'}))
]

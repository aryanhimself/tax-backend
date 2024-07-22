from django.urls import path
from rest_framework.routers import DefaultRouter
from _auth.views import AuthViewSet
from django.views.decorators.csrf import ensure_csrf_cookie

router = DefaultRouter()
router.register(r'', AuthViewSet, basename='auth')

urlpatterns = [
    path('login/', ensure_csrf_cookie(AuthViewSet.as_view({'post': 'login'}))),
    path('logout/', AuthViewSet.as_view({'post': 'logout'})),
    path('signup/', AuthViewSet.as_view({'post': 'signup'})),
    path('me/', AuthViewSet.as_view({'get': 'me'})),
]

urlpatterns += router.urls
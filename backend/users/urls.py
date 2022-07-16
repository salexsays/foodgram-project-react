from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

# from .views import UserViewSet


router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('users/me/', UserView.as_view(), name='me'),
]

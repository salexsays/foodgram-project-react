from django.urls import include, path, re_path
# from rest_framework.routers import DefaultRouter

# from .views import FollowViewSet

# app_name = 'users'

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('users/<int:author_id>/subscribe/',
    #     FollowViewSet.as_view({'get': 'create', 'delete': 'destroy'}),
    #     name='subscribe'),
    # path('users/subscriptions/', FollowViewSet.as_view({'get': 'list'}),
    #      name='subscriptions'),
    # path('', include(router.urls)),
]

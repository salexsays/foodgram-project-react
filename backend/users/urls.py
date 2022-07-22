from api.views import FollowViewSet
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path(
    #     'users/<int:author_id>/subscribe/',
    #     FollowViewSet.as_view({'post': 'create', 'delete': 'destroy'}),
    #     name='subscribe'
    # ),
    # path(
    #     'users/subscriptions/',
    #     FollowViewSet.as_view({'get': 'list'}),
    #     name='subscriptions'
    # ),
]

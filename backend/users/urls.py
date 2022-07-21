from api.views import FollowViewSet
from django.urls import include, path, re_path

app_name = 'users'

urlpatterns = [
    path('', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns = [
    path(
        'users/<int:author_id>/subscribe/',
        FollowViewSet.as_view({'post': 'create', 'delete': 'destroy'}),
        name='subscribe'
    ),
    path(
        'users/subscriptions/',
        FollowViewSet.as_view({'get': 'list'}),
        name='subscriptions'
    ),
]

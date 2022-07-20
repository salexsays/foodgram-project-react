from django.urls import include, path, re_path

# from djoser import views
from api.views import FollowViewSet

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
#     path('', include('djoser.urls')),
#     path('auth/token/login/', views.TokenCreateView.as_view(), name='login'),
#     path('auth/token/logout/', views.TokenDestroyView.as_view(),
#          name='logout'),
]

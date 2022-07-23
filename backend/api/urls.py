from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    DownloadShoppingCart,
    IngredientsViewSet,
    RecipeViewSet,
    TagsViewSet,
)  # FollowViewSet)

app_name = 'api'

router = DefaultRouter()

router.register(r'tags', TagsViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')


urlpatterns = [
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
    path(
        'recipes/download_shopping_cart/',
        DownloadShoppingCart.as_view(),
        name='dowload_shopping_cart',
    ),
    path('', include(router.urls)),
]

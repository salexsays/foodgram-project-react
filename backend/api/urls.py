from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DownloadShoppingCart, FollowViewSet,
                    IngredientsViewSet, RecipeViewSet, 
                    TagsViewSet)

app_name = 'api'

router = DefaultRouter()

router.register(r'tags', TagsViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')


urlpatterns = [
    path('users/<int:author_id>/subscribe/',
        FollowViewSet.as_view({'get': 'create', 'delete': 'destroy'}),
        name='subscribe'),
    path('users/subscriptions/', FollowViewSet.as_view({'get': 'list'}),
         name='subscriptions'),
    path('recipes/download_shopping_cart/',
         DownloadShoppingCart.as_view(), name='dowload_shopping_cart'),

    # path(
    #     'recipes/<int:recipe_id>/shopping_cart/',
    #     ShoppingCartView.as_view(),
    #     name='shopping_cart'
    # ),
    # path(
    #     'recipes/download_shopping_cart/',
    #     download_shopping_cart,
    #     name='download_shopping_cart'
    # ),

#     path(
#         'users/subscriptions/',
#         SubscribeListViewSet.as_view({'get': 'list'}),
#         name='subscriptions'
#     ),
    # path(
    #     'recipes/<int:recipe_id>/shopping_cart/',
    #     ShoppingCartViewSet.as_view(),
    #     name='shopping_cart'
    # ),
#     path(
#         'recipes/<int:recipe_id>/favorite/',
#         FavoriteViewSet.as_view(),
#         name='favorite'
#     ),
#     path(
#         'users/<int:user_id>/subscribe/',
#         SubscribeView.as_view(),
#         name='follow'
#     ),
    path('', include(router.urls)),
]

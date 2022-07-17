from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    TagViewSet,
    RecipeViewSet,
    IngredientViewSet,
    ShoppingCartView,
    download_shopping_cart
#     FavoriteViewSet,
#     ShoppingCartViewSet,
#     SubscribeListViewSet,
#     SubscribeView,
#     # UsersViewSet,
)

app_name = 'api'

router = DefaultRouter()
# # router.register(r'users', UsersViewSet)
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')


urlpatterns = [
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        ShoppingCartView.as_view(),
        name='shopping_cart'
    ),
    path(
        'recipes/download_shopping_cart/',
        download_shopping_cart,
        name='download_shopping_cart'
    ),

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

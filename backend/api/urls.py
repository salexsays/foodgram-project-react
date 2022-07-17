from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    TagViewSet,
    RecipeViewSet,
#     FavoriteViewSet,
#     IngredientViewSet,

#     ShoppingCartViewSet,
#     SubscribeListViewSet,
#     SubscribeView,

#     # UsersViewSet,
)

app_name = 'api'

router = DefaultRouter()
# # router.register(r'users', UsersViewSet)
router.register(r'recipes', RecipeViewSet, basename='recipes')
# router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'tags', TagViewSet, basename='tags')


urlpatterns = [
#     path(
#         'users/subscriptions/',
#         SubscribeListViewSet.as_view({'get': 'list'}),
#         name='subscriptions'
#     ),
#     # path('', include('djoser.urls')),
#     # path('auth/', include('djoser.urls.authtoken')),
#     path(
#         'recipes/<int:recipe_id>/shopping_cart/',
#         ShoppingCartViewSet.as_view(),
#         name='shopping_cart'
#     ),
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

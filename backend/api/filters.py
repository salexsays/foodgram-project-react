from django_filters import rest_framework as filters

from recipes.models import Ingredient, Recipe


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(
        method='get_favorite',
    )
    is_in_shopping_cart = filters.BooleanFilter(
        method='get_shopping',
    )

    class Meta:
        model = Recipe
        fields = ('is_favorited', 'author', 'tags', 'is_in_shopping_cart')

    def get_favorite(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(
                favorite_recipe__user=self.request.user
            )
        return Recipe.objects.all()

    def get_shopping(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(shopping_cart__user=self.request.user)
        return Recipe.objects.all()

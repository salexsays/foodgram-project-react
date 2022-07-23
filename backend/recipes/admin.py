from django.contrib import admin

from .models import (
    Favorite,
    Ingredient,
    IngredientAmount,
    Recipe,
    ShoppingCart,
    Tag,
)


class IngredientAmountInLine(admin.TabularInline):
    model = IngredientAmount


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'count_favorites')
    list_filter = ('author', 'name', 'tags')
    inlines = [IngredientAmountInLine]

    def count_favorites(self, obj):
        return obj.favorites.count()


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)

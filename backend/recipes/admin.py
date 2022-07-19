from django.contrib import admin

from .models import Recipe, Ingredient, Tag, Favorite, IngredientAmount, ShoppingCart


class IngredientAmountInLine(admin.TabularInline):
    model = IngredientAmount


class IngredientAdmin(admin.ModelAdmin):
    list_filter = (
        'id',
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author'
    )
    list_filter = (
        'author',
        'name',
        'tags'
    )
    inlines = [IngredientAmountInLine]
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug'
    )
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'user'
    )


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe'
    )


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)

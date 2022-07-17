from django.contrib import admin

from .models import Recipe, Ingredient, Tag, Favorite, RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
    )
    list_filter = (
        'author',
        'name',
        'tags'
    )


class IngredientAdmin(admin.ModelAdmin):
    list_filter = (
        'id',
        'name',
        'measurement_unit',
    )
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug'
    )


class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'recipe',
        'user'
    )


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ingredient',
        'recipe',
        'amount'
    )

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

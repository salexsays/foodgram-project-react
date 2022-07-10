from django.contrib import admin

from .models import Recipe, Ingredient  #, Tag


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


# class TagAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'color',
#         'slug'
#     )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(Tag, TagAdmin)

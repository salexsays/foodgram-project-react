from django.contrib import admin

from .models import User, Subscribe


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name'
    )
    list_filter = (
        'email',
        'username',
    )
    search_fields = ('username', 'email',)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author',
    )
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Subscribe, SubscribeAdmin)

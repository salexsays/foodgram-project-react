from django.contrib import admin

from .models import User, Follow


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'password'
    )
    list_filter = ('email', 'username',)
    search_fields = ('username', 'email',)


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)

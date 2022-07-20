from rest_framework import serializers
# from rest_framework.serializers import ValidationError

from .models import User, Follow
# from recipes.models import Recipe
# from api.serializers import RecipeSerializer


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'id', 'username',
            'first_name', 'last_name', 'is_subscribed'
        )

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request is None or request.user.is_anonymous:
            return False
        return Follow.objects.filter(
            user=request.user, author=obj
        ).exists()


# class FollowSerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField(source='author.id')
#     email = serializers.ReadOnlyField(source='author.email')
#     username = serializers.ReadOnlyField(source='author.username')
#     first_name = serializers.ReadOnlyField(source='author.first_name')
#     last_name = serializers.ReadOnlyField(source='author.last_name')
#     is_subscribed = serializers.SerializerMethodField()
#     recipes = serializers.SerializerMethodField()
#     recipes_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Follow
#         fields = ('id', 'email', 'username', 'first_name', 'last_name',
#                   'is_subscribed', 'recipes', 'recipes_count')
    
#     def validate_following(self, following):
#         if self.context.get('request').method == 'POST':
#             if self.context.get('request').user == following:
#                 raise ValidationError('Нельзя подписаться на себя')
#         return following

#     def get_is_subscribed(self, obj):
#         return Follow.objects.filter(
#             user=obj.user, author=obj.author
#         ).exists()

#     def get_recipes(self, obj):
#         request = self.context.get('request')
#         limit = request.GET.get('recipes_limit')
#         queryset = Recipe.objects.filter(author=obj.author)
#         if limit:
#             queryset = queryset[:int(limit)]
#         return RecipeSerializer(queryset, many=True).data

#     def get_recipes_count(self, obj):
#         return Recipe.objects.filter(author=obj.author).count()

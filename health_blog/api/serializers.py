from rest_framework import serializers
from .models import Articles, Comments
from django.contrib.auth.models import User
from .commentSerializer import CommentSerializer

# To convert python model to JSON
class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Articles
        fields = '__all__'
        extra_kwargs = {"author": {"read_only": True}}
    def get_author(self, obj):
        if 'populate_author' in self.context and self.context['populate_author']:
            author = obj.author
            return {
                'id': author.id,
                'username': author.username,
                'email': author.email
            }
        else:
            return None 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username' ,'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


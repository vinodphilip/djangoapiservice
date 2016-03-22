from django.contrib.auth.models import User
from .models import Post, Comment
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('url','title','slug','description','userId','body')


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('url','postId','name','email','body','comment_date')
from django.forms import ModelForm
from .models import Post, Comment


class AddPostForm(ModelForm):
    class Meta:
     	model = Post
     	exclude = ['id']
     	

class AddPostCommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ['id']
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User,null=True)
    body = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s'% self.title

        
class Comment(models.Model):
    postId = models.ForeignKey(Post)
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(blank=True)
    body = models.TextField(blank=True)
    comment_date = models.DateTimeField('comment date')
    
    def __unicode__(self):
        return self.name


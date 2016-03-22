from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangoapi.views.home', name='home'),
    # /posts/
    url(r'^$', views.get_post, name='getpost'),
    
    # /posts/add/
    url(r'^add/$', views.add_post, name='addpost'),
    
    # /posts/save/
    url(r'^save/$', views.save_post, name='savepost'),

    # /posts/1/
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name='postdetail'),
    
    #/posts/1/comments
    url(r'^(?P<post_id>[0-9]+)/comments/$', views.get_comment, name='getcomments'),
    
    url(r'^add/comment/$', views.add_comment, name='addcomment'),
	
	# /posts/save/
    url(r'^comment/save/$', views.save_comment, name='savecomment'),

]
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.template import loader
from .forms import AddPostForm, AddPostCommentForm

import requests

def _url(path):
    return 'http://jsonplaceholder.typicode.com' + path


def get_post(request):

	result = requests.get(_url('/posts/'))
	json = result.json()
	
	return HttpResponse(result)

    
def post_detail(request, post_id):
    
    result = requests.get(_url('/posts/'+post_id+'/'))

    return HttpResponse(result)


def get_comment(request, post_id):

	result = requests.get(_url('/posts/'+post_id+'/comments/'))

	return HttpResponse(result)


def comment_detail(request, comment_id):

	result = request.get(_url('/comment/'+comment_id+'/'))

	return HttpResponse(result)


def add_comment(request):

    form = AddPostCommentForm()
    template = loader.get_template('blog/add_comment.html')
    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def add_post(request):
     
    form = AddPostForm()
    template = loader.get_template('blog/add_post.html')
    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def save_post(request):

	if request.method == "POST":
		form = AddPostForm(request.POST)
        if form.is_valid():
		    result =  requests.post(_url('/posts/'), data={
            'title': form.cleaned_data['title'],
            'body': form.cleaned_data['description'],
            'userId':form.cleaned_data['userId'].id
            })
		    return HttpResponse(result)   

	else:
		return HttpResponse('Not a post method')

def save_comment(request):

	if request.method == "POST":
		form = AddPostCommentForm(request.POST)
        if form.is_valid():
		    result =  requests.post(_url('/posts/comment/'), data={
            'postId': form.cleaned_data['postId'].id,
            'name': form.cleaned_data['name'],
            'email':form.cleaned_data['email'],
            'body': form.cleaned_data['body']
            })
		    return HttpResponse(result)   

	else:
		return HttpResponse('Not a post method')	

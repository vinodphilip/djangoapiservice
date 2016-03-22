from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from blog import views
from django.views.generic import TemplateView
# Router provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'post', views.PostViewSet)
#router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^posts/', include('blog.urls')),
    #url(r'^', include(router.urls)),
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

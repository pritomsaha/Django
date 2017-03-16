from django.conf.urls import url
from . import views
app_name = 'posts'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^detail/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name = 'details'),
	url(r'^create/$', views.PostCreateView.as_view(), name = 'createPost' ),
	url(r'^update/(?P<slug>[-\w]+)/$', views.PostUpdateView.as_view(), name = 'updatePost'),
	url(r'^delete/(?P<slug>[-\w]+)/$', views.post_delete, name = 'deletePost'),
	
]
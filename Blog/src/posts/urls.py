from django.conf.urls import url
from . import views
from .Views import views as new_View
app_name = 'posts'
urlpatterns = [
	url(r'^$', new_View.IndexView.as_view(), name = 'index'),
	url(r'^detail/(?P<slug>[-\w]+)/$', new_View.DetailView.as_view(), name = 'details'),
	url(r'^create/$', new_View.PostCreateView.as_view(), name = 'createPost' ),
	url(r'^update/(?P<slug>[-\w]+)/$', new_View.PostUpdateView.as_view(), name = 'updatePost'),
	url(r'^delete/(?P<slug>[-\w]+)/$', new_View.post_delete, name = 'deletePost'),
	url(r'^createPDF/(?P<slug>[-\w]+)/$', new_View.createPDF, name = 'createPDF'),
	
]
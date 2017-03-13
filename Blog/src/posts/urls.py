from django.conf.urls import url
from . import views
app_name = 'posts'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^detail/(?P<id>[0-9]+)/$', views.DetailView.as_view(), name = 'details')

]
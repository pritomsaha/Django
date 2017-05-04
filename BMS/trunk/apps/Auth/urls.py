from django.conf.urls import url
from .views import *

app_name = 'Auth'
urlpatterns = [
	url(r'^$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^change_password/$', change_password, name='change_password'),
	url(r'^my-profile/$', user_profile, name='user_profile'),
	url(r'^users/save/$', user_save, name='user_save'),
	url(r'^users/save/(?P<id>[\w]+)/$', user_save, name='user_save'),
	url(r'^users/delete/(?P<id>[\w]+)/$', user_delete, name='user_delete'),
	url(r'^users/index/$', user_index, name='user_index'),
]
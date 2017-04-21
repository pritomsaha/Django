from django.conf import settings
from django.db import models

# Create your models here.

def upload_location(instance, filename):
	return "%s/%s" %(instance.timestamp.year, filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	title = models.CharField(max_length = 220)
	slug = models.SlugField(unique = True)
	image = models.ImageField(upload_to = 'images/', null = True, blank = True,
			width_field = 'width_field', height_field = 'height_field')
	height_field = models.IntegerField(default = 0)
	width_field = models.IntegerField(default = 0)
	content = models.TextField()
	draft = models.BooleanField(default = False)
	publish = models.DateTimeField(auto_now = False, auto_now_add = False)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	def __str__(self):
	  	return self.title

	class Meta:
		ordering = ['-timestamp', '-updated']

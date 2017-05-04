from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	return "%s/%s" %(instance.timestamp.year, filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	title = models.CharField(max_length = 220)
	slug = models.SlugField(unique = True)
	image = models.ImageField(upload_to = 'images/', null = True, blank = True,
			width_field = 'width_field', height_field = 'height_field')
	height_field = models.IntegerField(default = 0, null = True)
	width_field = models.IntegerField(default = 0, null = True)
	content = models.TextField()
	draft = models.BooleanField(default = False)
	publish = models.DateField(auto_now = False, auto_now_add = False)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

	objects = PostManager()

	def __str__(self):
	  	return self.title

	class Meta:
		ordering = ['-timestamp', '-updated']

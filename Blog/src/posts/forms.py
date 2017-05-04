import itertools

from django import forms
from django.utils.text import slugify
from pagedown.widgets import PagedownWidget
from .models import Post

class PostForm(forms.ModelForm):
	content = forms.CharField(widget =  PagedownWidget)
	publish = forms.DateField(widget = forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			'title',
			'image',
			'content',
			'draft',
			'publish'
		]

	def save(self):
		instance = super(PostForm, self).save(commit = False)
		instance.slug = orig = slugify(instance.title)
		if self.instance.pk:
			search = Post.objects.filter(slug = instance.slug)
			if not search.exists() or search[0].pk == self.instance.pk:
				return super(PostForm, self).save()
		
		for x in itertools.count(1):
			if not Post.objects.filter(slug = instance.slug).exists():
				break
			instance.slug = "%s-%d" % (orig, x)
		instance.save()
		
		return instance	
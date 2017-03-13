from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
# Create your views here.

class IndexView(View):
	def get(self, request):
		posts = Post.objects.all()
		context = {
			'posts' : posts
		}
		return render(request, 'posts/index.html', context)

class DetailView(View):
	def  get(self, request, id = None):
		post = get_object_or_404(Post, pk=id)
		context = {
			'post' : post
		}
		return render(request, 'posts/details.html', context)
 		

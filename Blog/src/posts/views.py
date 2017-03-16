from django.utils.http import urlquote_plus
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views import View
from .models import Post
from .forms import PostForm
# Create your views here.

class IndexView(View):
	def get(self, request):
		paginator = Paginator(Post.objects.all(),5)
		page=request.GET.get('page')

		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)

		context = {
			'posts' : posts
		}
		return render(request, 'posts/index.html', context)

class DetailView(View):
	def  get(self, request, slug = None):
		post = get_object_or_404(Post, slug=slug)
		share_string = urlquote_plus(post.content)
		context = {
			'post' : post,
			'share_string' : share_string
		}
		return render(request, 'posts/details.html', context)

class PostCreateView(View):
	def get(self, request):
		form = PostForm()
		context = {
			'form': form 
		}
		return render(request, 'posts/create.html', context)

	def post(self, request):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

		form = PostForm(request.POST, request.FILES or None)
		if form.is_valid():
			instance = form.save()
			messages.success(request, "Post was successfully created")
			return redirect('posts:details', slug = instance.slug)
		else:
			context = {
				'form': form
			}
			messages.warning(request, "Post was not successfully created")
			return render(request, 'posts/create.html', context)


class PostUpdateView(View):
	def get(self, request, slug = None):
		instance = get_object_or_404(Post, slug = slug)
		form = PostForm(instance = instance)
		context = {
			'form': form 
		}
		return render(request, 'posts/create.html', context)

	def post(self, request, slug=None):
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

		instance = get_object_or_404(Post, slug = slug)
		form = PostForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			instance = form.save()
			messages.success(request, "Post was successfully updated")
		else:
			messages.warning(request, "Post was not successfully updated")

		return redirect('posts:details', slug = instance.slug)

def post_delete(request, slug = None):
	if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
			
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Post was successfully deleted")
	return redirect('posts:index')

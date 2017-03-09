from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import KirrURL
# Create your views here.

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	obj=get_object_or_404(KirrURL, shortcode__iexact=shortcode)
	return HttpResponseRedirect(obj.url)

class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj=get_object_or_404(KirrURL, shortcode__iexact=shortcode)
		return HttpResponseRedirect(obj.url)
	

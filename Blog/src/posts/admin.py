from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	fields = ('title', 'image', 'content', 'draft', 'publish')
	list_display = ["title", 'publish', "updated", "timestamp"]
	list_filter = ['updated', 'timestamp']
	search_fields = ['title', 'content']


admin.site.register(Post, PostModelAdmin)

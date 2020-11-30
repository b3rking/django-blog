from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'author', 'slug', 'status', 'publish')
	populated_fields = {'slug': ('title',)}
	search_fields = ('title', 'body')
	ordering = ('status', 'publish')

admin.site.register(Post, PostAdmin)
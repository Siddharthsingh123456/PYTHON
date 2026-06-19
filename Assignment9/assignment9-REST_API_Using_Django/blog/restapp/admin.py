from django.contrib import admin
from restapp.models import BlogPost



class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_by', 'created_on')
    list_filter = ('created_by','created_on')

# Register your models here.

admin.site.register(BlogPost, BlogPostAdmin)
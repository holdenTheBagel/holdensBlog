from django.contrib import admin
from .models import blogPost, Category, Profile, Comment
# Register your models here.
admin.site.register(blogPost)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)

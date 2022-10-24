from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
#from ckeditor.fields import RichTextField
from django.conf import settings
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse("details", args=(str(self.id)))
		return reverse('home')

	class Meta:
		ordering = ['-id']

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(blank=True, null=True, upload_to='images/profile/')
	twitter_url = models.CharField(max_length=255, null=True, blank=True)
	linkedIn_url = models.CharField(max_length=255, null=True, blank=True)
	github_url = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		#return reverse("details", args=(str(self.id)))
		return reverse('home')		

class blogPost(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#body = RichTextField(blank=True, null=True)
	header_image = models.ImageField(blank=True, null=True, upload_to='images/')
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	category = models.CharField(max_length=255, default='')
	snippet = models.CharField(max_length=100, default='')
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse("details", args=(str(self.id)))
		return reverse('home')

class Comment(models.Model):
	post = models.ForeignKey(blogPost, related_name='comments', on_delete=models.CASCADE)
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

	class Meta:

		ordering = ['-date_added']


from django import forms 
from .models import blogPost, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)

class postForm(forms.ModelForm):
	class Meta:
		model = blogPost
		fields = ('title', 'author', 'category', 'snippet', 'header_image', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'currentUser', 'type': 'hidden'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'snippet': forms.TextInput(attrs={'class': 'form-control'}), 
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

class editForm(forms.ModelForm):
	class Meta:
		model = blogPost
		fields = ('title', 'category', 'snippet', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'snippet': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'currentUser', 'type': 'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}


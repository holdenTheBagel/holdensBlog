from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from holdensblog_mainApp.models import Profile

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio', 'profile_pic', 'twitter_url', 'linkedIn_url', 'github_url']

		widgets = {
				'bio': forms.Textarea(attrs={'class': 'form-control'}),
				#'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
				#'author': forms.Select(attrs={'class': 'form-control'}),
				'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
				'linkedIn_url': forms.TextInput(attrs={'class': 'form-control'}), 
				'github_url': forms.TextInput(attrs={'class': 'form-control'}),
			}

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
	 	model = User
	 	fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2' )

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	#password = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	#last_login = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
	#is_superuser = forms.CharField(max_length=15, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_staff = forms.CharField(max_length=15, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_active = forms.CharField(max_length=15, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#date_joined = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
	 	model = User
	 	fields = ('username','first_name', 'last_name', 'email',)
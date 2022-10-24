from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ProfilePageForm
from holdensblog_mainApp.models import Profile, blogPost
# Create your views here.

class ProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
		context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
		context["page_user"] = page_user
		return context

	def get_user_posts(self, request):
		user_posts = blogPost.objects.filter(author=request.user)
		return render(request, {'user_posts': user_posts})

class CreateProfileView(CreateView):
	model = Profile
	form_class = ProfilePageForm
	template_name = 'registration/create_user_profile.html'
	

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
	model = Profile
	template_name = 'registration/edit_profile_page.html'
	form_class = ProfilePageForm
	#fields = ['bio', 'profile_pic', 'twitter_url', 'linkedIn_url', 'github_url']

class changePasswordsView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = reverse_lazy('home')

class userRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class userEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user
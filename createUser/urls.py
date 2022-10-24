from django.urls import path
from .views import userRegisterView, userEditView, changePasswordsView, ProfilePageView, EditProfilePageView, CreateProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', userRegisterView.as_view(), name='register'),
    path('edit_profile/', userEditView.as_view(), name='edit_profile'),
    path('password/', changePasswordsView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfileView.as_view(), name='create_profile_page'),
]

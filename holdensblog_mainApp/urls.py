from django.urls import path
from . import views
from .views import HomeView, DetailsView, addPostView, updatePostView, deletePostView, CategoryView, CategoryListView, LikeView, addCommentView, MainView 

urlpatterns = [
    #path('', views.home, name="home")
    path('', MainView.as_view(), name="main"),
    path('home/', HomeView.as_view(), name="home"),
    path('details/<int:pk>', DetailsView.as_view(), name="details"),
    path('make_a_post/', addPostView.as_view(), name="make_a_post"),
    path('details/update/<int:pk>', updatePostView.as_view(), name="update_post"),
    path('details/<int:pk>/delete', deletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('details/<int:pk>/comment/', addCommentView.as_view(), name="add_comment"),
   
]

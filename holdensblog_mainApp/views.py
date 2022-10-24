from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import blogPost, Category, Comment 
from .forms import postForm, editForm, commentForm 
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = blogPost
	template_name = 'home.html'
	ordering = ['-post_date']
	#ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class DetailsView(DetailView):
	model = blogPost
	template_name = 'details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DetailsView, self).get_context_data(*args, **kwargs)

		postLikes = get_object_or_404(blogPost, id=self.kwargs['pk'])
		total_likes = postLikes.total_likes()
		
		liked = False
		if postLikes.likes.filter(id=self.request.user.id).exists():
			liked = True
	
		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
	category_posts = blogPost.objects.filter(category=cats)
	return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts}) 

class addPostView(CreateView):
	model = blogPost
	form_class = postForm
	template_name = 'add_post.html'
	#fields = '__all__'

class updatePostView(UpdateView):
	model = blogPost
	form_class = editForm
	template_name = 'update_post.html'
	#fields = ['title', 'body']

class deletePostView(DeleteView):
	model = blogPost
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

def LikeView(request, pk):
	post = get_object_or_404(blogPost, id=request.POST.get('post_id'))
	liked = False	
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True	
	return HttpResponseRedirect(reverse('details', args=[str(pk)]))

class addCommentView(CreateView):
	model = Comment
	form_class = commentForm
	template_name = 'add_comment.html'

	def get_success_url(self):
		return reverse_lazy('details', kwargs={'pk': self.kwargs['pk']})
	
	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


class MainView(ListView):
	model = blogPost
	template_name = 'main.html'
	ordering = ['likes']
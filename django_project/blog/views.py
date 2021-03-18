from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('article-detailer', args=[str(pk)]))


class MyView(ListView):
    model = Post
    template_name = 'blog/myposts.html'
    ordering = ['-date_posted']


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add-post.html'
    # fields = ('title', 'snippet', 'category', 'content')
    # fields = ('title', 'author', 'snippet', 'category', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog-home')
# def home(request):context = {'posts': Post.objects.all()}return render(request, 'blog/home.html', context)


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = ['title', 'category', 'content']


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'blog/category.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


def about(request):
    return render(request, 'blog/about.html')

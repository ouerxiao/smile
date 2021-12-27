from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, PostImage
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

def post_detail_view(request, id):
    post = get_object_or_404(Post, id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'blog/detail.html', {
        'posts': posts,
        'photos': photos
    })

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def images(request):
    context = {
        'images': PostImage.objects.all()
    }
    return render(request, 'blog/images.html', context)
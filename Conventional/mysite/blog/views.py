#from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView


class PostListView(ListView):
    model = Post
    # template_name = "blog/post_list"
    # queryset = Post.objects.all()
    queryset = Post.objects.all().order_by('-modified_date')


class PostDetailView(DetailView):
    # template_name = "blog/post_detail"
    model = Post

class PostCreateView(CreateView):
    # template_name = "blog/post_form"
    model = Post
    fields = '__all__'

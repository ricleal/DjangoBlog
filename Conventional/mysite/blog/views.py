#from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'

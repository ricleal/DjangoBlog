#from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post


class PostDetailview(DetailView):
    model = Post

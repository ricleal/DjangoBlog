#coding: utf-8
from django.conf.urls import patterns, url
from blog.views import PostListView, PostDetailView,PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(),name='detail'),
    url(r'^create/$', PostCreateView.as_view(),name='create'),
]

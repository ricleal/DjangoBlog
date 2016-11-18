#coding: utf-8
from django.db import models
#from django.contrib.sites.models import Site

class Category(models.Model):
    '''

    '''
    title = models.CharField(max_length=256, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to="images/")
    published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog:detail', [self.pk])

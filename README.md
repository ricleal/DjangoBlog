# DjangoBlog
Tutorial for a Django Blog


# Introduction

![](https://f3f79d362f2f9272ed76ca8f1493bdd8d9ea59bd.googledrive.com/host/0B74beDyervjzWWdWY3lRYkJ4SGM/img/djangoExample.png)


# Resources:

- Classy Class-Based Views: https://ccbv.co.uk/
- Built-in class-based views API: https://docs.djangoproject.com/en/1.10/ref/class-based-views/


# Start

## Setup de environment

```bash
pip install --upgrade virtualenv
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

```

Test it:
```bash
python -c "import django; print(django.get_version())"
```

## Start the project:

```bash
django-admin startproject mysite
cd mysite/
tree
```

Output:
```
.
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Test it:
```bash
./manage.py runserver
```

Open: ```http://127.0.0.1:8000/```

## Start the app blog

```bash
python manage.py startapp blog
tree
```

Output:
```
.
├── db.sqlite3
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── mysite
    ├── __init__.py
    ├── __init__.pyc
    ├── settings.py
    ├── settings.pyc
    ├── urls.py
    ├── urls.pyc
    ├── wsgi.py
    └── wsgi.pyc
```

## Install the App:

`edit mysite/settings.py`.

Add `blog` to `INSTALLED_APPS`


## Create the Models

- Category
- Post


[Model field reference](https://docs.djangoproject.com/en/1.9/ref/models/fields/).

### Admin Site

`edit blog/admin.py`

Add:

```python
from .models import post, Phone

admin.site.register(post)
admin.site.register(Phone)

```

Let's create the models in the database:
```
./manage.py makemigrations
./manage.py migrate
```

Let's create a super user (admin/admin123) and play with the models in the Django Admin Interface:

```
python manage.py createsuperuser
```

```
./manage.py runserver
```

Go to: [http://localhost:8000/admin/](http://localhost:8000/admin/)

And add a few entries...

## Class Based Views

[Reference](https://docs.djangoproject.com/en/1.9/topics/class-based-views/)

### List

`edit blog/views.py`

```python
from django.views.generic import ListView
from blog.models import post

class postList(ListView):
    model = post
```

Create [blog/urls.py](mysite/blog/urls.py)

```python
from django.conf.urls import url
from blog.views import postList

urlpatterns = [
    url(r'^list/$', postList.as_view()),
]

```

`edit mysite/urls.py`.

Add `blog` to `urlpatterns`:

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]
```

#### Templates:

create: [blog/templates/blog/post_list.html](mysite/blog/templates/blog/post_list.html)

```
<html>
{% for object in object_list %}
  {{object}}
{% endfor %}
</html>

```

GO: http://localhost:8001/blog/list/

#### Templates: Let's make it better

mysite/blog/templates/blog/base.html

mysite/blog/templates/blog/post_list.html

GO: http://localhost:8001/blog/list/

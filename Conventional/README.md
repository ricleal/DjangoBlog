# DjangoBlog


# Introduction

- High-level Python Web Framework
- Quickly Develop Applications
- Built-In Security:
  - Cross-Site Request Forgery (CSRF)
  - Cross site scripting (XSS)
  - SQL injection protection
  - etc...
- Scalable
- Built-In Administrative Interface

## MVC vs MTV

- Model = Model
- View = Template
- Controller = View


![](https://i.stack.imgur.com/NLlwq.png)

# Start

## Setup de environment

```bash
pip install --upgrade virtualenv
virtualenv -p python3 venv
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

### Test it:

```bash
./manage.py runserver
```

Open: http://127.0.0.1:8000/

### Test Admin interface:

```
./manage.py migrate
```

Let's create a superuser (admin/admin123) and play with the models in the Django Admin Interface:

```
python manage.py createsuperuser
```

```
./manage.py runserver
```

Open: http://localhost:8000/admin/


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

Edit `mysite/settings.py`.

Add `blog` to `INSTALLED_APPS`


## Create the Models

- Category
- Post

[Model field reference](https://docs.djangoproject.com/en/1.9/ref/models/fields/).

```
./manage.py makemigrations
./manage.py migrate
```

## Get the new models on the Admin Site

`edit blog/admin.py`

Add:

```python
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
```

```
./manage.py runserver
```

Open: http://localhost:8000/admin/

## Create Views

Let's start with a `ListView` to list all the posts:

## Add new URLs

Add blog to global URLs:

Edit: `/mysite/urls.py`

Edit: `/mysite/blog/urls.py`

## Create Templates:

create: [blog/templates/blog/post_list.html](Conventional/mysite/blog/templates/blog/post_list.html)

```html
<html>
{% for object in object_list %}
  {{ object }}
  <hr/>
{% endfor %}
</html>

```

[Built-in template tags and filters](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/)

Go to: http://localhost:8001/blog/list/

#### Templates: Let's make it better

Create a base template:

`mysite/blog/templates/blog/base.html`

```html
<html>
{% block content %}Empty page{% endblock %}
</html>
```

Create the content:

`mysite/blog/templates/blog/post_list.html`


```html
{% extends 'base.html' %}
{% block content %}
{% for object in object_list %}
  {{ object }}
  <hr/>
{% endfor %}
{% endblock %}
```

GO: http://localhost:8001/blog/list/

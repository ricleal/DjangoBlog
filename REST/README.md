# DjangoBlog


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

`edit mysite/settings.py`.

Add `blog` to `INSTALLED_APPS`


## Create the Models

- Category
- Post

[Model field reference](https://docs.djangoproject.com/en/1.9/ref/models/fields/).

```
./manage.py makemigrations
./manage.py migrate
```

### Get the new models on the Admin Site

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


# Rest Framework

Add it to the site:

```
INSTALLED_APPS = (
    ...
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}
```

## Serializers

```
edit blog/serializers.py
```

Create:
```
CategorySerializer
PostSerializer
```

## View sets

```
edit blog/views.py
```

Create:
```
CategoryViewSet
PostViewSet
```

## Add the urls

```
edit my_site/urls.py
```
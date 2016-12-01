# DjangoBlog

Tutorial for a Django Blog

# Introduction

- High-level Python Web Framework
- Quickly Develop Applications
- ORM: Object-relational Mapper
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

![](http://wiki.openhatch.org/images/thumb/f/fd/Mtv-diagram.png/400px-Mtv-diagram.png)


## Serving Django web pages

- Django has a builtin Django webserver:
  - Never ever use in PRODUCTION
  - It has not gone through security audits or performance tests
- Use:
  - NGINX / Apache to serve static pages and forward Django requests to:
  - Gunicorn / uWSGI (WSGI - Web Server Gateway Interface - the Python standard for web servers and applications.)
    - Apache mod_wsgi
    - NGINX - communicate with WSGI with unix sockets / http:
    
    `the web client <-> the web server <-> the socket <-> uwsgi <-> Django`

![](https://i.stack.imgur.com/NLlwq.png)

# Django Default

![](Docs/imgs/django_conventional.png)

# Django REST Framework

![](Docs/imgs/django_rest.png)

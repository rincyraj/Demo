1. create venv and activate django_venv
2. django-admin startproject storefront
settings.py: Defines all  DB connections
asgi.py and wsgi.py: used for deployment
urls.py: defines urls or endpoints. it defines how client is connecting to which endpoints
manage.py: is a wrapper of django-admin
if we type django-admin: it provides list of commands[python manage.py and django-admin]
(django_venv) D:\RINCY\project\storefront>python manage.py

django-admin
python manage.py runserver <port> optional
http://127.0.0.1:8000/

Creation of app:
python manage.py startapp svt_app
whenever creates an app, go to settings.py

views.py(request handler)
request-->response

steps:
first add function in views.pyand 
2.add urls.py inside svt_app to call this function and urls.py inside store_front

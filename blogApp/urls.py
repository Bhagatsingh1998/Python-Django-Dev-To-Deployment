# it will be similar to urls.py which is in 'blog' app

from django.urls import path
# import views file so that we can call our 'home' function
# '.' current directory
from . import views

urlpatterns = [
  # 1st arg: it is for url. pur url is empty which means when user goes on our website ('/') 
  # 2nd arg: what should happen when that url is triggered. we are calling home function which should get executed
  # 3rd arg: giving the name for this path
  path('', views.home, name='blog-home'),
  path('about/', views.about, name='blog-about')
]

# mapping these routes to our main urls.py file
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path

# importing includes
from django.urls import path, include

urlpatterns = [
    # NOTE: its a good practice to put tralling slash at the end.
        # why? because bydefault it has trailing slash then django will redirect routes without adding a trailing slash to that route that has one. 
        # eg: path('blog_dev/', include('blogApp.urls')),
        # so both this blog_dev without a tralling slash and blog_dev with the tralling slash will get redirected to the blog routes  
        # https://dev.to/learndjango/trailing-url-slashes-in-django-4bf
        # https://stackoverflow.com/questions/42212122/why-django-urls-end-with-a-slash

    # now specifying the url patterent, which route should go to our blogApp urls
    # path('blog/', include('blogApp.urls')),

    # we want blogApp home page should be landing page ie localhost:8000
    path('', include('blogApp.urls')),
    path('admin/', admin.site.urls),
]

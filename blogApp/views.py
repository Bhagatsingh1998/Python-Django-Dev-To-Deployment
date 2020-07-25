from django.shortcuts import render
# importing http
from django.http import HttpResponse

# creating a function home which will handle the traffic from our home page of our blog
# this function will be responsible what user sees ion the page

# it take 'request' an arg. although we will not use but it has be present.
def home(request):
  # simple http reponse telling the use its a home page
  return HttpResponse('<h1>Blog Home </h1>')

def about(request): 
  return HttpResponse('<h1>Blog About</h1>')

# we have craeted a view but havent careted a route(url) to go to this page. creating a new file 'urls.py' within this app.  
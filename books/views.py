from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.

def books(request):
    currentBooks = Book.objects.all().values()
    template = loader.get_template('home.html')
    context ={
        'currentBooks': currentBooks
    }
    return HttpResponse(template.render(context, request))

def book(request, id):
    thisBook = Book.objects.get(id=id)
    template = loader.get_template('Book.html')
    context={
        'book': thisBook
    }
    return HttpResponse(template.render(context, request))

# other pages
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

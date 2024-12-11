from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book
from django.core.exceptions import ValidationError


# Create your views here.

def home(request):
    currentBooks = Book.objects.all()[:4].values()
    template = loader.get_template('home.html')
    context ={
        'currentBooks': currentBooks
    }
    return HttpResponse(template.render(context, request))

def books(request):
    currentBooks = Book.objects.all().values()
    template = loader.get_template('books.html')
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


def add_book(request): 
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        year = request.POST.get('year')
        rating = request.POST.get('rating')
        description = request.POST.get('description')
        cover = request.POST.get('cover')
        errors = []

        if not title or not author or not isbn or not year or not rating or not description or not cover:
            errors.append("All fields are required.")

        if errors:
            return render(request, 'add_book.html', {'errors': errors})

        try:
            Book.objects.create(Title=title,Author=author,ISBN=isbn,year=year,rating=rating,Description=description,Cover=cover)
            return redirect('books')  
        except ValidationError as e:
            errors.extend(e.messages)
            return render(request, 'add_book.html', {'errors': errors})

    return render(request, 'add_book.html')

# other pages
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

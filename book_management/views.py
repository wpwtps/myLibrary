from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from book_management.models import Category, Book

# Create your views here.
def index(request):
    header_str = 'Hello, Python variable'
    #template = loader.get_template('index.html')
    context = {
        'var1': header_str ,
        'cat_num': len(Category.objects.all()),
        'book_num': len(Book.objects.all())
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)
from django.shortcuts import render
from .models import *


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__iexact='a').count()
    num_authors = Authors.objects.all().count()
    context = {
        num_books: num_books,
        num_instances: num_instances,
        num_instances_available: num_instances_available,
        num_authors: num_authors
    }
    return render(request, 'index.html', context=context)

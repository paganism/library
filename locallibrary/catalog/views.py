from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import *


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__iexact='a').count()
    num_authors = Author.objects.all().count()
    num_fiction_genres = Genre.objects.filter(name__icontains='fiction').count()
    num_direct_book = Book.objects.filter(title__icontains='dune').count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fiction_genres': num_fiction_genres,
        'num_direct_book': num_direct_book,
        'num_visits': num_visits
    }
    return render(request, 'index.html', context=context)


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1

    def get_queryset(self):
        return Author.objects.all()
    

class AuthorDetailView(generic.DetailView):
    model = Author


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

    def get_queryset(self):
        return Book.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is some data'
        return context

class BookDetailView(generic.DetailView):
    model=Book

# The other way. Function view

# def book_detail_view(request,pk):
#     try:
#         book_id=Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")

#     #book_id=get_object_or_404(Book, pk=pk)
    
#     return render(
#         request,
#         'catalog/book_detail.html',
#         context={'book':book_id,}
#     )

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    paginate_by = 2
    template_name = 'catalog/bookinstance_list_borrowed_user.html'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class BorrowedBooksByUserListView(PermissionRequiredMixin, LoginRequiredMixin, generic.ListView):
    model = BookInstance
    paginate_by = 5
    template_name = 'catalog/bookinstance_list_borrowed.html'
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

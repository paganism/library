from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books' ),
    path('books/<pk>', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', BorrowedBooksByUserListView.as_view(), name='borrowed'),
]

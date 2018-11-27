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
    path('book/<pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/<pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('author/<pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
    path('book/create/', BookCreate.as_view(), name='book_create'),
    path('book/<pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('book/<pk>/delete/', BookDelete.as_view(), name='book_delete'),
]

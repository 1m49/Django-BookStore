from django.shortcuts import render
from django.views import generic
from .models import Book
from django.urls import reverse_lazy


# show list of books
class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# detail of books
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


# add book to website (create book)
class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_create.html'


# update books
class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book_list')


# delete books
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

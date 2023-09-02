from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Book
from .forms import CommentForm


# show list of books
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# detail of books
# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    book_comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.book = book
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, '✅ نظر شما با موفقیت ثبت گردید ، از همراهی شما سپاسگزاریم ', 'success')
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comment_form': comment_form,
        'comments': book_comments,
    })


# add book to website (create book)
class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'cover', 'author', 'translator', 'publisher', 'description', 'price']
    template_name = 'books/book_create.html'


# update books
class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'cover', 'author', 'translator', 'publisher', 'description', 'price', ]
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book_list')


# delete books
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

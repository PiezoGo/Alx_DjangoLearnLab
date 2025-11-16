from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('books.can_view', raise_exception=True)
def book_lists(request):
    books = Book.objects.all()
    return render(request, "books/book_lists.html", {"books": books})

@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
        )
        return redirect("book_lists")
    return render(request, "books/create_book.html")

@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_lists")
    return render(request, "books/edit_book.html", {"book": book})

@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_lists")

# Create your views here.

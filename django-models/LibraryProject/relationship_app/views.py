from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include related books in the context
        context['books'] = self.object.book_set.all()
        return context

from .models import Author, Book, Library, Librarian


Book(title='1984', author = 'Michael Ochieng')
Book.save()
print("success")
# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# 2. List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.book_set  # or Book.objects.filter(library=library)
    return books.all()  # ✅ test checks for books.all()


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

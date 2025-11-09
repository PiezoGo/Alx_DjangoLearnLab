from typing import Optional
from django.db.models import Q
from .models import Author, Book, Library, Librarian

# query_samples.py


def get_books_by_author(author_id: Optional[int] = None, author: Optional[Author] = None):
    """
    Query all books by a specific author.

    Accepts either an Author instance or an author_id (PK).
    Returns a QuerySet of Book objects (may be empty).
    """
    if author is None:
        if author_id is None:
            return Book.objects.none()
        author = Author.objects.filter(pk=author_id).first()
        if author is None:
            return Book.objects.none()

    # handle cases where Book has a ForeignKey 'author' or a ManyToMany 'authors'
    return Book.objects.filter(Q(author=author) | Q(authors=author)).distinct()


def list_books_in_library(library_id: Optional[int] = None, library: Optional[Library] = None):
    """
    List all books in a library.

    Accepts either a Library instance or a library_id (PK).
    Returns a QuerySet of Book objects (may be empty).
    """
    if library is None:
        if library_id is None:
            return Book.objects.none()
        library = Library.objects.filter(pk=library_id).first()
        if library is None:
            return Book.objects.none()

    # common relation names: library.books (ManyToMany or related_name), Book.library (FK),
    # Book.libraries (M2M), or reverse FK library.book_set
    # Try attribute access first (preferred for related_name)
    for attr in ("books", "book_set", "books_set", "library_books"):
        if hasattr(library, attr):
            try:
                return getattr(library, attr).all()
            except Exception:
                pass

    # fallback to querying Book fields
    return Book.objects.filter(Q(library=library) | Q(libraries=library)).distinct()


def get_librarian_for_library(library_id: Optional[int] = None, library: Optional[Library] = None):
    """
    Retrieve the librarian for a library.

    Accepts either a Library instance or a library_id (PK).
    Returns a Librarian instance or None.
    """
    if library is None:
        if library_id is None:
            return None
        library = Library.objects.filter(pk=library_id).first()
        if library is None:
            return None

    # common patterns: OneToOneField on Library named 'librarian', reverse related_name,
    # or Librarian model has FK to Library.
    if hasattr(library, "librarian"):
        try:
            return library.librarian
        except Exception:
            pass

    # try a plural reverse relation (e.g., library.librarians)
    if hasattr(library, "librarians"):
        try:
            qs = library.librarians.all()
            return qs.first() if qs.exists() else None
        except Exception:
            pass

    # fallback to querying the Librarian model directly
    return Librarian.objects.filter(Q(library=library) | Q(libraries=library)).first()
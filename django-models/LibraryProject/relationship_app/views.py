from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View

# Base CBV with role check
class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    role = None  # should be overridden in subclasses

    def test_func(self):
        user_profile = getattr(self.request.user, 'userprofile', None)
        return user_profile is not None and user_profile.role == self.role


# Admin View
class admin_view(RoleRequiredMixin, View):
    role = 'Admin'

    def get(self, request):
        return render(request, 'admin_view.html')


# Librarian View
class Librarian(RoleRequiredMixin, View):
    role = 'Librarian'

    def get(self, request):
        return render(request, 'librarian_view.html')


# Member View
class Member(RoleRequiredMixin, View):
    role = 'Member'

    def get(self, request):
        return render(request, 'member_view.html')

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# User Logout
def LogoutView(request):
    logout(request)
    
    messages.info(request, "You have successfully logged out.")
    return redirect('login')


# relationship_app/list_books.html
#relationship_app/library_detail.html", "library", "from .models import Library
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/list_books.html', context)

class LibraryDetailView(DetailView):
  model = Book
  template_name = 'books/book_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() 

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/reister.html'
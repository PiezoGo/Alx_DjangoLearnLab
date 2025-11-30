from django.urls import path
from .views import ListView,DeleteView,DetailView,UpdateView,CreateView

urlpatterns = [
    path('books/', ListView.as_view(), name='list'),
    path('books/<int:pk>', DetailView.as_view(), name='details'),
    path('books/update', UpdateView.as_view(), name='update'),
    path('books/delete', DeleteView.as_view(), name='delete'),
    path('books/create', CreateView.as_view(), name='new_book'),
    path('books/search/', BookSearchView.as_view(), name='book-search'),
    path('books/ordering/', BookOrderingView.as_view(), name='book-ordering'),
    path('books/my-books/', UserBookListView.as_view(), name='user-books'),
    path('books/user/<str:username>/', BookFilterByUsernameView.as_view(), name='books-by-username'),
]

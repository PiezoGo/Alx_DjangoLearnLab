from django.urls import path
from .views import ListView,DeleteView,DetailView,UpdateView,CreateView

urlpatterns = [
    path('books/', ListView.as_view(), name='list'),
    path('books/<int:pk>', DetailView.as_view(), name='details'),
    path('books/update', UpdateView.as_view(), name='update'),
    path('books/delete', DeleteView.as_view(), name='delete'),
    path('books/create', CreateView.as_view(), name='new_book'),
]

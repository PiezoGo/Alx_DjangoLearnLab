from django.urls import path
from .views import ListView,DeleteView,DetailView,UpdateView,CreateView

urlpatterns = [
    path('books/', ListView.as_view(), name='list'),
    path('books/<int:pk>', DetailView.as_view(), name='details'),
    path('books/<int:pk>/update', UpdateView.as_view(), name='update'),
    path('books/<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('books/new', CreateView.as_view(), name='new_book'),
]

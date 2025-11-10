from django.urls import path
from .views import list_books, BookDetailView

urlpatterns = [
   path('',  list_books, name='library'),
   path('detail/<int:pk>', BookDetailView.as_view(), name='detail')

]
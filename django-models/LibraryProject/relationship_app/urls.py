from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
   path('',  list_books, name='library'),
   path('detail/<int:pk>', LibraryDetailView.as_view(), name='detail')

]
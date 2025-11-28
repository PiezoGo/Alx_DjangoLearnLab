from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from .views import BookViewSet,BookList

router = DefaultRouter()

router.register(r'books-all', BookViewSet, basename='book_all')

urlpatterns = [
    #Route for boolklist View
    path('books/', BookList.as_view(), name = 'book-list'),
    #Include the routter urls BookViewset all CRUD operations
    path('',include(router.urls))
]
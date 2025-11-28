from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from .views import BookViewSet,BookList
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register(r'books-all', BookViewSet, basename='book_all')

urlpatterns = [
    #Route for boolklist View
    path('books/', BookList.as_view(), name = 'book-list'),
    #Include the routter urls BookViewset all CRUD operations
    path('',include(router.urls))
    path('api-token-auth/', obtain_auth_token),

]
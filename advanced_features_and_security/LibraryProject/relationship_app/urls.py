from django.urls import path
from .views import list_books,LibraryDetailView,LoginView,LogoutView,Admin, Librarian, Member
from . import views

urlpatterns = [
   path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('register/', views.register, name='register'),
   path('',  list_books, name='library'),
   path('detail/<int:pk>', LibraryDetailView.as_view(), name='detail'),
   path('admin-view/', Admin.as_view(), name='admin_view'),
   path('librarian-view/', Librarian.as_view(), name='librarian_view'),
   path('member-view/', Member.as_view(), name='member_view'),
   path('add_book/', views.add_book, name='add_book'),
   path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
   path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

]
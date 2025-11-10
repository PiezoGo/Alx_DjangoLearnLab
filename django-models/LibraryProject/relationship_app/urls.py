from django.urls import path
from .views import list_books,LibraryDetailView,LoginView,LogoutView
from . import views

urlpatterns = [
   path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('register/', views.register, name='register'),
   path('',  list_books, name='library'),
   path('detail/<int:pk>', LibraryDetailView.as_view(), name='detail')
   path('admin-view/', views.admin_view, name='admin_view'),
   path('librarian-view/', views.librarian_view, name='librarian_view'),
   path('member-view/', views.member_view, name='member_view'),

]
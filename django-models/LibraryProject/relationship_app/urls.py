from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
   path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('',  list_books, name='library'),
   path('detail/<int:pk>', LibraryDetailView.as_view(), name='detail')

]
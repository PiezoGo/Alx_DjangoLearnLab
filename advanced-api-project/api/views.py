from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer
from . import permissions

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [permissions.AllowAny]
    
    # Required filter backends
    filter_backends = [
        django_filters.DjangoFilterBackend,  # For filtering
        filters.SearchFilter,                # For searching  
        filters.OrderingFilter               # For ordering
    ]
    
    # Filtering by exact attributes
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Search functionality
    search_fields = ['title', 'author']
    
    # Ordering
    ordering_fields = ['title', 'author', 'publication_year', 'price']
    ordering = ['-created_at']

class UserBookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]
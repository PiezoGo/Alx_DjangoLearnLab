from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from . import permissions

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'description']
    ordering_fields = ['title', 'author', 'publication_year', 'price']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author__icontains=author)
        
        genre = self.request.query_params.get('genre')
        if genre:
            queryset = queryset.filter(genre=genre)
        
        year = self.request.query_params.get('publication_year')
        if year:
            queryset = queryset.filter(publication_year=year)
        
        year_min = self.request.query_params.get('publication_year_min')
        if year_min:
            queryset = queryset.filter(publication_year__gte=year_min)
        
        year_max = self.request.query_params.get('publication_year_max')
        if year_max:
            queryset = queryset.filter(publication_year__lte=year_max)
        
        price_min = self.request.query_params.get('price_min')
        if price_min:
            queryset = queryset.filter(price__gte=float(price_min))
        
        price_max = self.request.query_params.get('price_max')
        if price_max:
            queryset = queryset.filter(price__lte=float(price_max))
        
        return queryset

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
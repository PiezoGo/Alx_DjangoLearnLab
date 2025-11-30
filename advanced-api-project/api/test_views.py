from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')
        
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2023,
            'genre': 'FICTION',
            'isbn': '1234567890',
            'price': '29.99'
        }
        
        self.book = Book.objects.create(owner=self.user, **self.book_data)

    def test_list_books_unauthenticated(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_unauthenticated(self):
        response = self.client.post('/api/books/create/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/api/books/create/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book_owner(self):
        self.client.login(username='testuser', password='testpass')
        update_data = {'title': 'Updated Book'}
        response = self.client.patch(f'/api/books/{self.book.id}/update/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_update_book_non_owner(self):
        User.objects.create_user(username='other', password='otherpass')
        self.client.login(username='other', password='otherpass')
        update_data = {'title': 'Hacked Book'}
        response = self.client.patch(f'/api/books/{self.book.id}/update/', update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_owner(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_author(self):
        response = self.client.get('/api/books/?author=Test Author')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get('/api/books/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        Book.objects.create(
            owner=self.user,
            title='Another Book',
            author='Another Author',
            publication_year=2020,
            genre='FICTION',
            isbn='0987654321',
            price='19.99'
        )
        response = self.client.get('/api/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')

    def test_user_books_endpoint(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/books/my-books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
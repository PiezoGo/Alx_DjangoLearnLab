from rest_framework import serializers
from .models import Author, Book
from datetime import date
year = date.today()


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fiels = ['title', 'publication_year', 'author']

    def validate(self, data):
        if data['publication_year'] > year.year:
            raise serializers.ValidationError('This year you hav inputed is invalid!!')
        return data

class AuthorSerializer(serializers.ModelSerializer):
    Book = BookSerializer(many = True,read_only = True)
    class Meta:
        model = Author
        fields = ['name']


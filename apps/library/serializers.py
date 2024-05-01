from rest_framework import serializers
from .models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        lookup_field = 'id'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'id'


class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'
        lookup_field = 'id'

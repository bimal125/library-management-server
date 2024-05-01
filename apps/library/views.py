from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count


from .models import Author, Category, Book
from .serializers import (
    AuthorSerializer,
    CategorySerializer,
    BookSerializer,
)
from .filters import BookFilter


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing author instances.
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    serializer_class = BookSerializer
    filterset_class = BookFilter
    queryset = Book.objects.select_related('category', 'author')


class LibraryStatView(APIView):
    """
    A viewset to count number of books
    """

    def get(self, request, format=None):
        book_qs = Book.objects.aggregate(
            total_book_count=Count('id'),
            total_category_count=Count('category_id'),
            total_author_count=Count('author_id'),
        )
        return Response(book_qs)

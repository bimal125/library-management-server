import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'name': ['exact', 'contains'],
            'author__first_name': ['exact', 'contains'],
            'author__middle_name': ['contains'],
            'author__last_name': ['contains'],
        }

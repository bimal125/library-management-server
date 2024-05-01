from django.contrib import admin
from .models import Author, Category, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'created_at', 'updated_at']
    search_fields = [
        'id', 'first_name', 'middle_name', 'last_name'
    ]
    list_display_links = ['id', 'first_name']
    ordering = [
        'id', 'first_name', 'middle_name', 'last_name'
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = [
        'id', 'name'
    ]
    list_display_links = ['id', 'name']
    ordering = ['id', 'name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'created_at', 'updated_at']
    search_fields = ['name', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

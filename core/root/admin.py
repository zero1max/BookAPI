from django.contrib import admin
from .models import Book, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'publication_date', 'category')


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
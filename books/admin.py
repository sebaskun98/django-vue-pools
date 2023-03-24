from django.contrib import admin
from django.utils.text import get_text_list

from .models import Author, Book, Category, PublishingCompany


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(PublishingCompany)
class PCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'publishingCompany', 'category', 'author',
    )
    list_display_links = ('id', 'name',)
    list_filter = ('publishingCompany', 'category',)
    search_fields = ('id', 'name', 'author__name',)
    autocomplete_fields = ('author', 'publishingCompany', 'category')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('author')

    @admin.display(description='author')
    def authors_names(self, obj):
        names = list(obj.authors.values_list('name', flat=True))
        return get_text_list(names, last_word='and')

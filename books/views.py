from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import Author, Book, Category, Comment, PublishingCompany, Rating
from .serializers import AuthorSerializer, BookSerializer, CategorySerializer, CommentSerializer, \
    PublishingCompanySerializer, RatingSerializer


class AuthorPagination(PageNumberPagination):
    page_size = 10


class AuthorListAPIView(ModelViewSet):
    queryset = Author.objects.all()
    pagination_class = AuthorPagination
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]


class BookViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CategoryViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PCompanyViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = PublishingCompanySerializer
    queryset = PublishingCompany.objects.all()


class CommentViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class RatingViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        bookName = self.kwargs['name']
        return Book.objects.filter(name=bookName)

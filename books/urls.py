from django.urls import include, path

from rest_framework import routers

from .views import AuthorListAPIView, BookViewSet, PCompanyViewSet, RatingViewSet, CommentViewSet, CategoryViewSet

app_name = 'books'
router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorListAPIView)
router.register('pcompany', PCompanyViewSet)
router.register('rating', RatingViewSet)
router.register('comment', CommentViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

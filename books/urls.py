from django.urls import include, path, re_path

from rest_framework import routers

from .views import AuthorListAPIView, BookViewSet, PCompanyViewSet, RatingViewSet, CommentViewSet, CategoryViewSet, \
    BookList

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
    re_path('^book/(?P<name>.+)/$', BookList.as_view()),
]

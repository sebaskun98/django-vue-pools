from django.urls import path

from . import views
from .views import VoteView

app_name = 'polls'
urlpatterns = [
    path('', views.polls_list, name='index'),
    path('<int:pk>/', views.polls_detail, name='detail'),
    path('<int:pk>/results/', views.polls_results, name='results'),
    path('<int:pk>/vote', VoteView.as_view(), name='vote'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

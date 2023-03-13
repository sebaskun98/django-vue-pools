from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import ChoiceSerializer
from .models import Question, Choice
from rest_framework.mixins import UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from django_filters import rest_framework as filters

@api_view(http_method_names=['GET'])
def polls_results(request,pk):
    queryset = Choice.objects.all().values('id','choice_text','votes', 'question_id').filter(question_id = pk) 
    query_list = list(queryset)
    return JsonResponse(query_list, safe=False, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def polls_detail(request,pk):
    poll = get_object_or_404(Question, pk=pk)
    data = {
        "question": poll.question_text,
        "pub_date": poll.pub_date
    }
    return JsonResponse(data, status=status.HTTP_200_OK)
    
@api_view(http_method_names=['GET'])
def polls_list(request):
    data = list(Question.objects.all().values()[:20])
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('question_text', 'pub_date')
    return JsonResponse({
                            'questions': data},
                            safe=False, status=status.HTTP_200_OK)

class VoteView(GenericAPIView, UpdateModelMixin):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')
    
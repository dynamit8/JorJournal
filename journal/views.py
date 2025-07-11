from django_filters import rest_framework as filters

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Journal, Lesson
from .serializers import JournalSerializer, LessonSerializer
from .filters import LessonFilter

class JournalViewset(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class LessonViewset(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LessonFilter
    pagination_class = PageNumberPagination
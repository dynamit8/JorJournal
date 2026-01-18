from django_filters import rest_framework as filters
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Journal, Lesson
from .serializers import JournalSerializer, LessonSerializer
from .filters import LessonFilter
from .forms import JournalForm
from common.views import BaseTemplatePerModuleMixin

class APIJournalViewset(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class APILessonViewset(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LessonFilter
    pagination_class = PageNumberPagination

class JournalHomeView(BaseTemplatePerModuleMixin, TemplateView):
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'home.html'
    context_object_name = "journals"


class JournalListView(BaseTemplatePerModuleMixin, ListView):
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'list.html'
    context_object_name = "journals"


class JournalCreateView(BaseTemplatePerModuleMixin, CreateView):
    form_class = JournalForm
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'create.html'
    context_object_name = "journals"
    success_url = reverse_lazy('journal-create-success')

class JournalCreateSuccessView(BaseTemplatePerModuleMixin, TemplateView):
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'create_success.html'

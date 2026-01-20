from django_filters import rest_framework as filters
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Journal, Lesson
from .serializers import JournalSerializer, LessonSerializer
from .filters import LessonFilter
from .forms import JournalForm
from common.views import BaseTemplatePerModuleMixin
from tag.models import Tag

class APIJournalViewset(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class APILessonViewset(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LessonFilter
    pagination_class = PageNumberPagination

class JournalHomeView(BaseTemplatePerModuleMixin, LoginRequiredMixin, TemplateView):
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'home.html'
    context_object_name = "journals"


class JournalListView(BaseTemplatePerModuleMixin, LoginRequiredMixin, ListView):
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'list.html'
    context_object_name = "journals"
    queryset = Journal.objects.prefetch_related('tag').all()


class JournalCreateView(BaseTemplatePerModuleMixin, LoginRequiredMixin, CreateView):
    form_class = JournalForm
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'create.html'
    context_object_name = "journals"
    success_url = reverse_lazy('journal-create-success')

    def form_valid(self, form):
        tag_ids = []
        tag_input = form.cleaned_data.get("tag")
        if tag_input:
            tags = tag_input.split(" ")
            for tag in tags:
                try:
                    tag = Tag.objects.get(name=tag)
                except Tag.DoesNotExist:
                    tag = Tag.objects.create(name=tag)
                tag_ids.append(tag.id)
            form.cleaned_data["tag"] = tag_ids
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        existing_tags = Tag.objects.all().annotate(journals=Count("tagged_journals"))
        ophans = existing_tags.filter(journals=0)
        tagged = existing_tags.filter(journals__gt=0)
        kwargs.update({"tagged": tagged, "ophans": ophans})
        return kwargs

class JournalCreateSuccessView(BaseTemplatePerModuleMixin, LoginRequiredMixin, TemplateView):
    model = Journal
    TEMPLATE_DIR = 'journal'
    template_filename = 'create_success.html'

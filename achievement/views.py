from django.views.generic import TemplateView, ListView
from rest_framework.viewsets import ModelViewSet

from .models import Achievement
from .serializers import AchievementSerializer

from common.views import BaseTemplatePerModuleMixin

class APIAchievementViewset(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class AchievementHomeView(BaseTemplatePerModuleMixin, TemplateView):
    TEMPLATE_DIR = 'achievement'
    template_filename = 'home.html'
    context_object_name = "achievements"

class AchievementListView(BaseTemplatePerModuleMixin, ListView):
    TEMPLATE_DIR = 'achievement'
    template_filename = 'list.html'
    context_object_name = "achievements"
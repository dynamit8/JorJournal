
from .models import Achievement
from .serializers import AchievementSerializer


from rest_framework.viewsets import ModelViewSet

class APIAchievementViewset(ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
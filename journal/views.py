from rest_framework.viewsets import ModelViewSet

from .models import Journal
from .serializers import JournalSerializer

class JournalViewset(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
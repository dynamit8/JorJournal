from django_filters import rest_framework as filters

from .models import Lesson

class LessonFilter(filters.FilterSet):
    journal = filters.NumberFilter(field_name="journal__id")

    class Meta:
        model = Lesson
        fields = ["journal",]


    def filter(self, qs, value):
        print('fffffffffffffffffffffffffffffffffff')
        qs = super().filter(qs, value)
        print(qs.query)
        return qs
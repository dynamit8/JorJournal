from django.db import models

from journal.models import Journal

class Achievement(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    conditions = models.CharField(max_length=300)
    icon = models.ImageField(null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
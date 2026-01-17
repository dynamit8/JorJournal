from django.db import models

class Journal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.CharField(max_length=100)
    text = models.JSONField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.topic[:25]}..."
    
class Lesson(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ('topic',)

    def __str__(self):
        return f"{self.topic[:25]}..."
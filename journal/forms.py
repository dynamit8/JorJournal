
from django.forms import ModelForm
from django import forms
from .models import Journal

class JournalForm(ModelForm):
    tag = forms.CharField(max_length=200)
    class Meta:
        model = Journal
        fields = ["topic", "logs", "tag"]
from django.contrib import admin

from .models import Journal

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'created_at')
    search_fields = ('topic',)
    ordering = ('-created_at',)
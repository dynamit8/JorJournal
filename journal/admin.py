from django.contrib import admin

from .models import Journal, Lesson

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'created_at')
    search_fields = ('topic', 'tags')
    ordering = ('-created_at',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'journal')
    search_fields = ('topic',)
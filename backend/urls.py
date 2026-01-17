"""
URL configuration for JorJournal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from journal.views import APIJournalViewset, APILessonViewset
from achievement.views import APIAchievementViewset

router = routers.DefaultRouter()
router.register(r'api/journal', APIJournalViewset, basename='journal')
router.register(r'api/lesson', APILessonViewset, basename='lesson')
router.register(r'api/achievement', APIAchievementViewset, basename='achievement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
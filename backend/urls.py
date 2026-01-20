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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from rest_framework import routers
from common.views import LandingView
from journal.views import APIJournalViewset, APILessonViewset, JournalHomeView, JournalListView, JournalCreateView, JournalCreateSuccessView
from achievement.views import APIAchievementViewset, AchievementHomeView, AchievementListView

router = routers.DefaultRouter()
router.register(r'journal', APIJournalViewset, basename='apijournal')
router.register(r'lesson', APILessonViewset, basename='apilesson')
router.register(r'achievement', APIAchievementViewset, basename='apiachievement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    
    path('', LandingView.as_view(), name='landing'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    # journal
    path('journal/', JournalHomeView.as_view(), name='journal-home'),
    path('journal/list/', JournalListView.as_view(), name='journal-list'),
    path('journal/create/', JournalCreateView.as_view(), name='journal-create'),
    path('journal/create/success', JournalCreateSuccessView.as_view(), name='journal-create-success'),
    
    # path('journal/<int:pk>/', JournalDetailView.as_view(), name='journal-detail'),
    # achievement
    path('achievement/', AchievementHomeView.as_view(), name='achievement-home'),
    path('achievement/list/', AchievementListView.as_view(), name='achievement-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
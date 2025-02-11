from django.contrib import admin
from django.urls import path, include
from .views import get_project_kpi
from rest_framework.routers import DefaultRouter
from .views import ProjectKPIViewSet 
from . import views


router = DefaultRouter()
router.register(r'project-kpi', ProjectKPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('kpi/unique-state/', views.UniqueStateView.as_view(), name='unique-state'),
    path('kpi/unique-scheme/', views.UniqueSchemeView.as_view(), name='unique-scheme'),
    path('kpi/unique-project/', views.UniqueProjectView.as_view(), name='unique-project'),

]
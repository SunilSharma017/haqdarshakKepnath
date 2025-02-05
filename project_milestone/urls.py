from django.contrib import admin
from django.urls import path, include
from .views import get_project_milestone
from .views import ProjectMilestoneSerializer
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'project_milestone', ProjectMilestoneViewSet)

urlpatterns = [
    path('project_milestone/', views.get_project_milestone, name='get_project_milestone'), 
    # path('project_milestone/weekly/', views.get_project_milestone_weekly_data, name='get_project_milestone_weekly_data'),

]
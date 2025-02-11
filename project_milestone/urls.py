from django.contrib import admin
from django.urls import path, include
from .views import get_project_milestone
from .views import ProjectMilestoneSerializer
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('project_milestone/', views.get_project_milestone, name='get_project_milestone'), 

]
from django.contrib import admin
from django.urls import path, include
from .views import get_project_summary
from .views import ProjectSummaryViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'project_summary', ProjectSummaryViewSet)

urlpatterns = [
    # path('project_summary/', views.get_project_summary, name='get_project_summary'), 
    path('', include(router.urls)),
    path('api/unique-states/', views.UniqueStatesView.as_view(), name='unique-states'),
    path('api/unique-project/', views.UniqueProjectView.as_view(), name='unique-project'),
    path('api/unique-status/', views.UniqueStatusView.as_view(), name='unique-status'),
    path('api/unique-schemes/', views.UniqueClientsView.as_view(), name='unique-clients'),
]

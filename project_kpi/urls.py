from django.contrib import admin
from django.urls import path, include
from .views import get_project_kpi
from rest_framework.routers import DefaultRouter
from .views import ProjectKPIViewSet 
#top_ranked_applications
from . import views
# from .views import LeaderboardViewSet
# from .views import BestPerformance
# from .views import BottomPerformance


router = DefaultRouter()
router.register(r'project-kpi', ProjectKPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('kpi/unique-state/', views.UniqueStateView.as_view(), name='unique-state'),
    path('kpi/unique-scheme/', views.UniqueSchemeView.as_view(), name='unique-scheme'),
    path('kpi/unique-project/', views.UniqueProjectView.as_view(), name='unique-project'),

    # path('project_kpi/', get_project_kpi, name='get_project_kpi'), 
    # path('project_kpi/best/', BestPerformance.as_view(), name='get_best_performance'),
    # path('project_kpi/bottom/', BottomPerformance.as_view(), name='get_bottom_performance'),
]
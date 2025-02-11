

from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('project_summary.urls')),
    path('',include('project_kpi.urls')),
    path('',include('project_milestone.urls')),
    

]

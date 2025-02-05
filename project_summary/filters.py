import django_filters
from .models import project_summary

class ProjectSummaryFilter(django_filters.FilterSet):
    class Meta:
        model = project_summary
        fields = ['project_name','project_status','scheme_name','state']
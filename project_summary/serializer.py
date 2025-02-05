from rest_framework import serializers
from .models import project_summary




class UniqueStateSerializer(serializers.Serializer):
    state = serializers.CharField()
    class Meta:
        model=project_summary

class UniqueStatusSerializer(serializers.Serializer):
    project_status = serializers.CharField()

    class Meta:
        model=project_summary

class UniqueClientsSerializer(serializers.Serializer):
    scheme_name = serializers.CharField()

    class Meta:
        model=project_summary

class UniqueProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField()

    class Meta:
        model=project_summary

class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = project_summary
        fields= ['project_name','project_status', 'project_start_date', 'project_end_date', 'scheme_name','state', 'org_pid']
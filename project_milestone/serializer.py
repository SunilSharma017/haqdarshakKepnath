from rest_framework import serializers
from .models import project_milestone

class WeeklyDataSerializer(serializers.Serializer):
    week_start_date = serializers.DateField()
    week_end_date = serializers.DateField()
    applications_count = serializers.IntegerField()
    
class ProjectMilestoneSerializer(serializers.ModelSerializer):
    weekly_data = WeeklyDataSerializer(many=True)  # Include the weekly data
    class Meta:
        model = project_milestone
        fields = ['org_pid', 'project_name', 'project_start_date', 'project_end_date','weekly_data']


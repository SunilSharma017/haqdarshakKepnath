from rest_framework import serializers
from .models import project_kpi
from django.db.models import Sum
from rest_framework.response import Response

class ProjectKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = project_kpi
        fields = ['project_id','Application_Open_Count','Docket_Submitted_Count','Benefit_Received_Count','scheme_value','scheme_name','project_names','citizen_state'] 



class Projecttop5states(serializers.Serializer):
    state_name = serializers.CharField()
    Application_Open = serializers.IntegerField()


class UniqueStateSerializer(serializers.Serializer):
    citizen_state = serializers.CharField()
    class Meta:
        model=project_kpi

class UniqueSchemeSerializer(serializers.Serializer):
    scheme_name = serializers.CharField()
    class Meta:
        model=project_kpi

class UniqueProjectSerializer(serializers.Serializer):
    project_names = serializers.CharField()
    class Meta:
        model=project_kpi


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import project_summary
from .serializer import ProjectSummarySerializer
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import ProjectSummaryFilter
from .models import project_summary
from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def get_project_summary(request):
    project_summaries = project_summary.objects.using('default').all()
    serializer = ProjectSummarySerializer(project_summaries, many=True)
    
    return Response(serializer.data)

# For project_summary, we use a viewset with filtering capabilities


class ProjectSummaryViewSet(viewsets.ModelViewSet):
    queryset = project_summary.objects.all()
    serializer_class = ProjectSummarySerializer

    def get_queryset(self):
        # Get the base queryset
        queryset = super().get_queryset()

        # Get query parameters for filtering
        status = self.request.query_params.get('status', None)
        state = self.request.query_params.get('state', None)
        scheme = self.request.query_params.get('client', None)
        project = self.request.query_params.get('project', None)

        # Initialize filters dictionary
        filters = {}

        # Apply filters if the parameters are provided and not "All Status"/"All Schemes"/"All Projects"
        if status and status.strip() != "All Status":
            filters['project_status__iexact'] = status.strip()  # Case insensitive match
        if state and state.strip() != "All State":
            filters['state__iexact'] = state.strip()
        if scheme and scheme.strip() != "All Schemes":
            filters['scheme_name__iexact'] = scheme.strip()
        if project and project.strip() != "All Projects":
            filters['project_name__iexact'] = project.strip()

        # Apply filters to queryset
        queryset = queryset.filter(**filters)

        return queryset





def get_unique_states(request):
    # Get unique states from the ProjectSummary model
    unique_states = project_summary.objects.values('state').distinct()

    # If you want to return it as a JSON response
    return JsonResponse(list(unique_states), safe=False)


class UniqueStatesView(APIView):
    def get(self, request):
        # Get unique states from the Project table
        unique_states = project_summary.objects.values_list('state', flat=True).distinct()
        print(len(list(unique_states)))
        return Response({"states": list(unique_states)})

class UniqueClientsView(APIView):
    def get(self, request):
        # Get unique states from the Project table
        unique_clients = project_summary.objects.values_list('scheme_name', flat=True).distinct()
        return Response({"scheme_name": list(unique_clients)})
    

class UniqueProjectView(APIView):
    def get(self, request):
        # Get unique states from the Project table
        unique_project = project_summary.objects.values_list('project_name', flat=True).distinct()
        return Response({"project_name": list(unique_project)})

class UniqueStatusView(APIView):
    def get(self, request):
        # Get unique states from the Project table
        unique_status = project_summary.objects.values_list('project_status', flat=True).distinct()
        return Response({"project_status": list(unique_status)})


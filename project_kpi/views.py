from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import project_kpi
from .serializer import ProjectKPISerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.db.models import Sum
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum



class ProjectKPIViewSet(viewsets.ModelViewSet):
    queryset = project_kpi.objects.all()
    serializer_class = ProjectKPISerializer

    def get_leaderboard(self, queryset):
        """Returns the top 5 and bottom 5 states based on Application_Open_Count."""
        state_aggregation = (
            queryset.values("citizen_state")
            .annotate(
                total_applications=Sum("Application_Open_Count"),
                total_docket_submitted=Sum("Docket_Submitted_Count"),
                total_benefit_received=Sum("Benefit_Received_Count")
            )
            .order_by("-total_applications")
        )

        top_5_states = list(state_aggregation[:5])  
        bottom_5_states = list(state_aggregation.reverse()[:5])  

        return top_5_states, bottom_5_states

    def list(self, request, *args, **kwargs):
        scheme = request.query_params.get('scheme', None)
        state = request.query_params.get('state', None)
        project = request.query_params.get('project', None)

        filters = {}
        if scheme and scheme.strip() != "All":
            filters['scheme_name__iexact'] = scheme.strip()
        if state and state.strip() != "All":
            filters['citizen_state__iexact'] = state.strip()
        if project and project.strip() != "All":
            filters['project_names__iexact'] = project.strip()

        queryset = project_kpi.objects.filter(**filters)

        top_5_states, bottom_5_states = self.get_leaderboard(queryset)

        aggregated_data = queryset.aggregate(
            total_application_open=Sum('Application_Open_Count', default=0),
            total_docket_submitted=Sum('Docket_Submitted_Count', default=0),
            total_benefit_received=Sum('Benefit_Received_Count', default=0)
        )

        total_application_open = aggregated_data["total_application_open"] or 0
        total_docket_submitted = aggregated_data["total_docket_submitted"] or 0
        total_benefit_received = aggregated_data["total_benefit_received"] or 0
        print(top_5_states)
        print(bottom_5_states)
        
        return Response({
            "top5States": top_5_states,
            "bottom5States": bottom_5_states,
            "totalApplicationOpen": total_application_open,
            "totalDocketSubmitted": total_docket_submitted,
            "totalBenefitReceived": total_benefit_received
        })



@api_view(['GET'])
def get_project_kpi(request):
    aggregated = request.GET.get('aggregated', None)
    aggregated_data = project_kpi.objects.values('project_id') \
            .annotate(
                Application_Open_Count=Sum('Application_Open_Count'),
                Docket_Submitted_Count=Sum('Docket_Submitted_Count'),
                Benefit_Received_Count=Sum('Benefit_Received_Count'),
                scheme_value=Sum('scheme_value')
            )
    
    serializer = ProjectKPISerializer(aggregated_data, many=True)
    return Response(serializer.data)


class UniqueStateView(APIView):
    def get(self, request):
        unique_states = project_kpi.objects.values_list('citizen_state', flat=True).distinct()
        return Response({"citizen_state": list(unique_states)})

class UniqueSchemeView(APIView):
    def get(self, request):
        unique_schemes = project_kpi.objects.values_list('scheme_name', flat=True).distinct()
        return Response({"scheme_name": list(unique_schemes)})
    
class UniqueProjectView(APIView):
    def get(self, request):
        unique_project = project_kpi.objects.values_list('project_names', flat=True).distinct()
        return Response({"project_names": list(unique_project)})
       

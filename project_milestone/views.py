from datetime import timedelta, datetime
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import project_milestone, project_milestone_apps_open
from .serializer import ProjectMilestoneSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # You can adjust the page size here
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def get_project_milestone(request):
    project_milestones = project_milestone.objects.using('default').all()

    results = []

    for milestone in project_milestones:
        if isinstance(milestone.project_start_date, str):
            project_start_date = datetime.strptime(milestone.project_start_date, "%Y-%m-%d").date()
        else:
            project_start_date = milestone.project_start_date

        if isinstance(milestone.project_end_date, str):
            project_end_date = datetime.strptime(milestone.project_end_date, "%Y-%m-%d").date()
        else:
            project_end_date = milestone.project_end_date

        days_to_subtract = project_start_date.weekday() + 1  # Monday is 0, Sunday is 6
        week_start_date = project_start_date - timedelta(days=days_to_subtract)

        current_date = week_start_date  # Start from the Sunday before project_start_date
        weekly_data = []

        while current_date <= project_end_date:
            week_end_date = current_date + timedelta(days=6)  # Saturday is 6 days from Sunday

            if week_end_date > project_end_date:
                week_end_date = project_end_date  # Ensure it doesn't go beyond project_end_date

            weekly_sum = project_milestone_apps_open.objects.filter(
                created_date__gte=current_date,
                created_date__lte=week_end_date,
                project_id=milestone.org_pid  # Correct join on project_id
            ).aggregate(week_sum=Sum('Application_Open_Count'))['week_sum'] or 0

            weekly_data.append({
                'week_start_date': current_date,
                'week_end_date': week_end_date,
                'applications_count': weekly_sum,
            })

            current_date = week_end_date + timedelta(days=1)  # Move to the next Sunday

        result = {
            'org_pid': milestone.org_pid,
            'project_name': milestone.project_name,
            'project_start_date': milestone.project_start_date,
            'project_end_date': milestone.project_end_date,
            'weekly_data': weekly_data  # Pass the weekly data to the serializer
        }

        results.append(result)

    return Response(results)

from django.db import models

class project_milestone(models.Model):
    org_pid = models.CharField(max_length=100, primary_key=True)
    project_name = models.CharField(max_length=100)
    project_start_date = models.DateField()
    project_end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'pm_org_schemes_locations_mapping'

    def __str__(self):
        return self.project_name


class project_milestone_apps_open(models.Model):
    project_id = models.CharField(max_length=100)
    Application_Open_Count = models.IntegerField()
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'daily_aggregates'

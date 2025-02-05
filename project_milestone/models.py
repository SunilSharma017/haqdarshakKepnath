from django.db import models

# Create your models here.
class project_milestone(models.Model):
    org_pid = models.CharField(max_length=100, primary_key=True)
    project_name = models.CharField(max_length=100)
    # project_status = models.CharField(max_length=100)
    project_start_date = models.DateField()
    project_end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'pm_org_schemes_locations_mapping'

    def __str__(self):
        return self.project_name
    

# Create your models here.
class project_milestone_apps_open(models.Model):
    project_id = models.CharField(max_length=100)
    Application_Open_Count = models.IntegerField()
    created_date = models.DateField()
    # Docket_Submitted_Count = models.IntegerField()
    # Benefit_Received_Count = models.IntegerField()
    # scheme_value = models.IntegerField()
    # scheme_name = models.CharField(max_length=100)
    

    class Meta:
        managed = False
        db_table = 'daily_aggregates'
        # unique_together = (('project_id', 'scheme_name'),)
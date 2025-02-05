from django.db import models

# Create your models here.
class project_kpi(models.Model):
    project_id = models.CharField(max_length=24,primary_key=True)
    Application_Open_Count = models.IntegerField()
    Docket_Submitted_Count = models.IntegerField()
    Benefit_Received_Count = models.IntegerField()
    scheme_value = models.IntegerField()
    scheme_name = models.CharField(max_length=100)
    project_names=models.CharField(max_length=100)
    citizen_state=models.CharField(max_length=100)
    class Meta:
        db_table = 'daily_aggregates'
        # unique_together = (('project_id', 'scheme_name'),)
    def __str__(self):
        return self.project_names



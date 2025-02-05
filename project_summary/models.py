from django.db import models

# Create your models here.

class project_summary(models.Model):
    project_name = models.CharField(max_length=100)
    scheme_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    project_status = models.CharField(max_length=100)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    org_pid = models.CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = 'pm_org_schemes_locations_mapping'

    def __str__(self):
        return self.project_name
    
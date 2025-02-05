# Generated by Django 5.0.9 on 2025-01-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('scheme_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('project_status', models.CharField(max_length=100)),
                ('project_start_date', models.DateField()),
                ('project_end_date', models.DateField()),
                ('pid', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pm_org_schemes_location_mapping',
            },
        ),
    ]

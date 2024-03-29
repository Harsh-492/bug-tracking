# Generated by Django 5.0.2 on 2024-03-04 09:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_rename_enddate_project_end_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='end_date',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='start_date',
            new_name='startDate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_img',
        ),
        migrations.AddField(
            model_name='project',
            name='projectimg',
            field=models.ImageField(null=True, upload_to='project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='estimated_hours',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projectteam',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterField(
            model_name='projectteam',
            name='status',
            field=models.CharField(blank=True, choices=[('Started', 'Started'), ('Complted', 'Complted'), ('Working', 'Working'), ('Debuging', 'Debuging')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projectteam',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='project',
            table='project',
        ),
        migrations.AlterModelTable(
            name='projectteam',
            table='projectteam',
        ),
    ]

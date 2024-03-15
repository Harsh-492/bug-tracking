# Generated by Django 5.0.2 on 2024-02-27 10:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_project_module'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelTable(
            name='project_module',
            table='project_module',
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('totalMinutes', models.IntegerField()),
                ('Module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project_module')),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'db_table': 'Task',
            },
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
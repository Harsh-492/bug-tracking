# Generated by Django 5.0.2 on 2024-03-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_task_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='endTime',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_remove_projectteam_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Started', 'Started'), ('Complted', 'Complted'), ('Processing', 'Processing')], max_length=100, null=True),
        ),
    ]

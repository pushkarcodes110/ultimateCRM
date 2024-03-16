# Generated by Django 5.0.3 on 2024-03-16 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_plan_alter_team_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='teams.plan'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-16 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_plan_max_clients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='plan',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
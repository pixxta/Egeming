# Generated by Django 4.2.7 on 2023-11-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egeming_app', '0002_task_subject_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subject_type',
            field=models.CharField(default='No subject', max_length=50),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-18 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egeming_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subject_type',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

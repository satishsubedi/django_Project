# Generated by Django 2.2 on 2020-06-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0026_patientcheckupinfo_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientcheckupinfo',
            name='result',
        ),
        migrations.AddField(
            model_name='patientcheckupinfo',
            name='result',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
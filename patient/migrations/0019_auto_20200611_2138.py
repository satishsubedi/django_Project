# Generated by Django 2.2 on 2020-06-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0018_auto_20200611_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinformation',
            name='testdetails',
            field=models.TextField(blank=True, null=True),
        ),
    ]

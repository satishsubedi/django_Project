# Generated by Django 2.2 on 2020-06-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_remove_patienttransaction_lab_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienttransaction',
            name='lab_item',
            field=models.ManyToManyField(to='hospital.ExaminationType'),
        ),
    ]

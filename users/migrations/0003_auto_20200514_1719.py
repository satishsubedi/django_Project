# Generated by Django 2.2 on 2020-05-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_delete_hospitaldoctor'),
        ('users', '0002_auto_20200510_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='degree',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ManyToManyField(related_name='hospital', to='hospital.Hospital'),
        ),
        migrations.AddField(
            model_name='examiner',
            name='degree',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examiner',
            name='hospital',
            field=models.ManyToManyField(related_name='examiner_hospital', to='hospital.Hospital'),
        ),
        migrations.AddField(
            model_name='examiner',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examiner',
            name='lab_details',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examiner',
            name='license_id',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='speciality',
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ManyToManyField(related_name='speciality', to='users.DoctorSpeciality'),
        ),
    ]

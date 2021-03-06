# Generated by Django 2.2 on 2020-05-17 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200514_1719'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('remarks', models.TextField()),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_doctor', to='users.Doctor')),
                ('patient_check_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='findings', to='patient.PatientCheckupInfo')),
            ],
        ),
    ]

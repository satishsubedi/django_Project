# Generated by Django 2.2 on 2020-06-08 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_remove_examinationtype_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0010_auto_20200607_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('vat', models.FloatField()),
                ('grandtotal', models.FloatField()),
                ('paidby', models.CharField(choices=[('online', 'online'), ('cash', 'cash'), ('other', 'other')], max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('lab_item', models.ManyToManyField(related_name='lab_item', to='hospital.ExaminationType')),
                ('lab_rate', models.ManyToManyField(related_name='lab_rate', to='hospital.ExaminationType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_trxn_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2 on 2020-05-10 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0002_auto_20200509_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='hospital_created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/hospitals/%Y-%m-%d/'),
        ),
    ]

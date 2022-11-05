# Generated by Django 4.1.1 on 2022-09-14 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='assignDoctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_document4', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='assignNurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_document5', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='assignRelative',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_document6', to=settings.AUTH_USER_MODEL),
        ),
    ]

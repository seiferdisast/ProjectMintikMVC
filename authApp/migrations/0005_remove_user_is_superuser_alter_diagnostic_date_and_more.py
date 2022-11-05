# Generated by Django 4.1.1 on 2022-09-17 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authApp", "0004_alter_user_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_superuser",
        ),
        migrations.AlterField(
            model_name="diagnostic",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="diagnostic",
            name="patient_documentId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patient_diagnosticated",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="vitalsigns",
            name="patient_documentId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vital_signs_patient",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="vitalsigns",
            name="vitalSignsDate",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

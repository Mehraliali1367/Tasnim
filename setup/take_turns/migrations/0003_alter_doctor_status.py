# Generated by Django 4.0.5 on 2022-06-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take_turns', '0002_doctor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

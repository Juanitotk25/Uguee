# Generated by Django 5.0.6 on 2025-05-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituciones', '0002_alter_institucion_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institucion',
            name='logo',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
    ]

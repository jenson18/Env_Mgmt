# Generated by Django 3.0.6 on 2020-05-29 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Env_Register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envlist_new',
            name='Release',
            field=models.CharField(max_length=10),
        ),
    ]

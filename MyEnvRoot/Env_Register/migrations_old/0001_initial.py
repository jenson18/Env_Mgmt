# Generated by Django 3.0.6 on 2020-05-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvList_New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VAPP', models.CharField(max_length=20)),
                ('BSS_Non_CPQ', models.CharField(max_length=20)),
                ('CPQ_OSS_SIO', models.CharField(max_length=20)),
                ('ARM', models.CharField(max_length=20)),
                ('DB_SERVERS', models.CharField(max_length=500)),
                ('COMMENTS', models.CharField(max_length=500)),
                ('CREATION_DATE', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

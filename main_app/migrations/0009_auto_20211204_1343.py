# Generated by Django 3.2.9 on 2021-12-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]

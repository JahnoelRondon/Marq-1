# Generated by Django 3.2.9 on 2021-12-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_todo_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='importance',
            field=models.CharField(choices=[('Important', 'Important'), ('General', 'General'), ('Minor', 'Minor')], default='General', max_length=20),
        ),
    ]

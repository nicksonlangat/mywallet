# Generated by Django 2.0.1 on 2020-05-06 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='picture',
        ),
    ]

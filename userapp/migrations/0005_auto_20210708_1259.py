# Generated by Django 3.2.3 on 2021-07-08 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20210707_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='item',
        ),
        migrations.RemoveField(
            model_name='details',
            name='user',
        ),
    ]
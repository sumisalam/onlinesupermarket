# Generated by Django 3.2.3 on 2021-07-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20210708_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

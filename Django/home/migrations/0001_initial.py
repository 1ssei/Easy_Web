# Generated by Django 2.0a1 on 2018-03-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('max_temperature', models.IntegerField(default=0)),
                ('min_temperature', models.IntegerField(default=0)),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-14 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25, unique=True)),
                ('joined', models.DateTimeField(default=datetime.datetime(2021, 3, 14, 8, 32, 35, 814817, tzinfo=utc))),
                ('is_anonymous', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=15)),
            ],
        ),
    ]

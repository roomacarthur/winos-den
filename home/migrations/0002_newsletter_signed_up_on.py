# Generated by Django 3.2.14 on 2022-07-29 21:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='signed_up_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 29, 21, 48, 7, 803582, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

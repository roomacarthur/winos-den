# Generated by Django 3.2.14 on 2022-07-30 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsletter_signed_up_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name_plural': 'News Letter'},
        ),
    ]

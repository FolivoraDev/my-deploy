# Generated by Django 2.1.3 on 2018-12-28 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20181219_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-01 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='star',
            new_name='review_avg',
        ),
    ]

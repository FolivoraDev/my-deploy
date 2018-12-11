# Generated by Django 2.1.3 on 2018-12-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='request',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='menu_summary',
            field=models.ManyToManyField(blank=True, to='restaurants.Food'),
        ),
    ]
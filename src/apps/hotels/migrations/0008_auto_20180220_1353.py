# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20180220_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodtime',
            options={'verbose_name': 'food time', 'verbose_name_plural': 'food times'},
        ),
        migrations.RemoveField(
            model_name='hotelroom',
            name='food_info',
        ),
        migrations.RemoveField(
            model_name='roomfoodinfo',
            name='cost',
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='capacity',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='capacity'),
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotels.RoomType', verbose_name='type'),
        ),
        migrations.AddField(
            model_name='roomfoodinfo',
            name='cost_info',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_food_info', to='hotels.FoodCost', verbose_name='cost info'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('booking_confirmed', 'booking confirmed'), ('booking_not_confirmed', 'booking not confirmed'), ('occupied', 'occupied'), ('alert', 'alert')], default='booking_not_confirmed', max_length=32, verbose_name='payment status'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-06-07 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_rename_guest_number_booking_guess_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guess_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]

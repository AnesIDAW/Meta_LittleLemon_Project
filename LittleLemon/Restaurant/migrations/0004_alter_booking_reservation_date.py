# Generated by Django 5.0.3 on 2024-06-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0003_remove_booking_comment_remove_booking_guess_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(),
        ),
    ]
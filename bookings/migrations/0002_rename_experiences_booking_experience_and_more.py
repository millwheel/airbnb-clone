# Generated by Django 4.2.4 on 2023-09-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="experiences",
            new_name="experience",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="rooms",
            new_name="room",
        ),
        migrations.AddField(
            model_name="booking",
            name="check_out",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="experience_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

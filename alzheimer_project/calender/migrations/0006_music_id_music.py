# Generated by Django 4.2.7 on 2023-11-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calender", "0005_activity_time_alter_activity_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="id_music",
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]

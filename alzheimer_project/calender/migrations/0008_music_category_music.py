# Generated by Django 4.2.7 on 2023-11-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calender", "0007_rename_name_music_name_music"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="category_music",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

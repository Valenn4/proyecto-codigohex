# Generated by Django 4.2.7 on 2023-11-16 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("calender", "0002_action_music_object_activity_id_game_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="activity",
            name="description",
        ),
        migrations.RemoveField(
            model_name="activity",
            name="name",
        ),
        migrations.RemoveField(
            model_name="activity",
            name="type",
        ),
        migrations.AlterField(
            model_name="activity",
            name="id_action",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calender.action",
            ),
        ),
        migrations.AlterField(
            model_name="activity",
            name="id_game",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calender.game",
            ),
        ),
        migrations.AlterField(
            model_name="activity",
            name="id_music",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calender.music",
            ),
        ),
        migrations.AlterField(
            model_name="activity",
            name="id_object",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calender.object",
            ),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_codigo_postal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codigo_postal',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_codigo_postal_alter_user_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codigo_postal',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True),
        ),
    ]
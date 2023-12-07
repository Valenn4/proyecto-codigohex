# Generated by Django 4.2.7 on 2023-12-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codigo_postal',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='etapa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='medicacion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='numero_telefono',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True),
        ),
    ]
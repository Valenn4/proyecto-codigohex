# Generated by Django 4.2.7 on 2023-12-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='user.jpg', upload_to='avatar/'),
        ),
    ]
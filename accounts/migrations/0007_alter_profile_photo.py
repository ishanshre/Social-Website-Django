# Generated by Django 4.1 on 2022-09-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='profile_photo/default.png', upload_to='profile_photo/%Y/%m/%d/'),
        ),
    ]

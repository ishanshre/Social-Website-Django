# Generated by Django 4.1 on 2022-09-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile_photo/%Y/%m/%d/'),
        ),
    ]

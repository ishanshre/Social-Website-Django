# Generated by Django 4.1 on 2022-09-09 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_post_options_post_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='follow',
        ),
    ]
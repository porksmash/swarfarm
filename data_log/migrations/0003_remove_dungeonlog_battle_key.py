# Generated by Django 2.1.7 on 2019-03-07 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_log', '0002_remove_dungeonsecretdungeondrop_monster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dungeonlog',
            name='battle_key',
        ),
    ]
# Generated by Django 2.1.7 on 2019-06-17 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_log', '0014_auto_20190615_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magicboxcraftrunecraftdrop',
            name='ancient',
        ),
        migrations.RemoveField(
            model_name='riftdungeonrunecraftdrop',
            name='ancient',
        ),
        migrations.RemoveField(
            model_name='riftraidrunecraftdrop',
            name='ancient',
        ),
    ]

# Generated by Django 2.2.17 on 2020-11-11 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0027_auto_20200901_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enemy',
            options={'ordering': ('order',), 'verbose_name_plural': 'Enemies'},
        ),
        migrations.AddField(
            model_name='monster',
            name='skill_group_id',
            field=models.IntegerField(blank=True, help_text='Identifier that matches same skillup monsters (i.e. Street Figher monsters with C2U counterparts)', null=True),
        ),
    ]
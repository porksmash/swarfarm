# Generated by Django 2.2.10 on 2020-02-23 18:46

import django.db.models.deletion
from django.db import migrations, models

import bestiary.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0022_auto_20200217_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Level')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('com2us_id', models.IntegerField()),
                ('boss', models.BooleanField(default=False)),
                ('stars', models.IntegerField(choices=[(1, '1⭐'), (2, '2⭐'), (3, '3⭐'), (4, '4⭐'), (5, '5⭐'), (6, '6⭐')])),
                ('level', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('resist', models.IntegerField()),
                ('crit_bonus', models.IntegerField()),
                ('crit_damage_reduction', models.IntegerField()),
                ('accuracy_bonus', models.IntegerField()),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Monster')),
                ('wave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Wave')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model, bestiary.models.base.Stars),
        ),
    ]
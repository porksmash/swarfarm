# Generated by Django 2.1.7 on 2019-04-21 06:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('bestiary', '0010_auto_20190318_1206'),
        ('data_log', '0009_auto_20190407_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_timestamp', models.DateTimeField()),
                ('end_timestamp', models.DateTimeField()),
                ('log_count', models.IntegerField()),
                ('unique_contributors', models.IntegerField()),
                ('report', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'get_latest_by': 'end_timestamp',
            },
        ),
        migrations.CreateModel(
            name='LevelReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data_log.Report')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='logs', to='bestiary.Level')),
            ],
            bases=('data_log.report',),
        ),
        migrations.CreateModel(
            name='SummonReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data_log.Report')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bestiary.GameItem')),
            ],
            bases=('data_log.report',),
        ),
        migrations.AddField(
            model_name='report',
            name='content_type',
            field=models.ForeignKey(blank=True, help_text='The logging model used to generate this report', null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
    ]
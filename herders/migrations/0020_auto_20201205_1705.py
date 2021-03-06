# Generated by Django 2.2.17 on 2020-12-06 01:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bestiary', '0028_auto_20201111_1135'),
        ('herders', '0019_auto_20201111_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialStorage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.GameItem')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herders.Summoner')),
            ],
            options={
                'ordering': ['item'],
            },
        ),
        migrations.CreateModel(
            name='MonsterShrineStorage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bestiary.Monster')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herders.Summoner')),
            ],
            options={
                'ordering': ['item'],
            },
        ),
    ]

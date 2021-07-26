# Generated by Django 3.1.3 on 2021-07-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Symbol', models.CharField(blank=True, max_length=200, null=True)),
                ('EntryPrice', models.FloatField(blank=True, null=True)),
                ('ExitPrice', models.FloatField(blank=True)),
                ('Performance', models.FloatField(blank=True, null=True)),
                ('VolumeChange', models.FloatField(blank=True, null=True)),
                ('InNifty50', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
                'db_table': 'Stocks',
                'ordering': ['Symbol'],
            },
        ),
    ]
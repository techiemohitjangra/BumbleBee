# Generated by Django 5.0.2 on 2024-02-26 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=256)),
                ('full_name', models.CharField(max_length=64)),
                ('message', models.TextField()),
                ('contact_time', models.DateTimeField(auto_now=True, verbose_name='submission_date_time')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phrase', models.CharField(max_length=64)),
                ('word_count', models.IntegerField()),
                ('start_time', models.TimeField(verbose_name='phrase_start_time')),
                ('end_time', models.TimeField(verbose_name='phrase_end_time')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_date_time', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=64)),
                ('start_time', models.DateTimeField(verbose_name='phrase_start_time')),
                ('end_time', models.DateTimeField(verbose_name='phrase_end_time')),
                ('from_phrase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speaker.phrase')),
            ],
        ),
    ]

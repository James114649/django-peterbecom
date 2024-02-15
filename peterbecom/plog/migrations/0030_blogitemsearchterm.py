# Generated by Django 4.2.10 on 2024-02-14 01:45

import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plog', '0029_auto_20201105_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogItemSearchTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=255, unique=True)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('search_vector_en', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('popularity', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

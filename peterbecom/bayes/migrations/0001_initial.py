# Generated by Django 2.0.7 on 2018-07-07 18:39

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plog', '0015_blogitem_open_graph_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BayesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickle_data', models.BinaryField()),
                ('options', django.contrib.postgres.fields.jsonb.JSONField()),
                ('topic', models.CharField(default='comments', max_length=100)),
                ('size', models.IntegerField()),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCommentTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bayes_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bayes.BayesData')),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plog.BlogComment')),
            ],
        ),
    ]

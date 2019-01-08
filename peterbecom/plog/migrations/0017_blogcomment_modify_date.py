# Generated by Django 2.1.5 on 2019-01-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plog', '0016_auto_20180802_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RunSQL(
            "UPDATE plog_blogcomment SET modify_date=add_date"
        )
    ]

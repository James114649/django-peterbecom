# Generated by Django 2.2.8 on 2020-01-01 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20190902_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postprocessing',
            name='previous',
            field=models.ForeignKey(db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postprocessing', to='base.PostProcessing'),
        ),
    ]

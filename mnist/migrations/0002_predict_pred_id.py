# Generated by Django 2.0.3 on 2019-04-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predict',
            name='pred_id',
            field=models.IntegerField(default=0),
        ),
    ]

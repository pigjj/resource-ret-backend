# Generated by Django 2.1 on 2019-02-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20190207_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='websocketchannel',
            name='disconnect',
            field=models.BooleanField(default=0),
        ),
    ]

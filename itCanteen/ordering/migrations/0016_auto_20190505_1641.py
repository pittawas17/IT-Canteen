# Generated by Django 2.2 on 2019-05-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0015_auto_20190505_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]

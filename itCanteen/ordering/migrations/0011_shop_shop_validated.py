# Generated by Django 2.2 on 2019-05-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0010_auto_20190505_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_validated',
            field=models.BooleanField(default=False),
        ),
    ]
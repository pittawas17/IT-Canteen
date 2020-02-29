# Generated by Django 2.2 on 2019-05-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0028_remove_shop_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='cold_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='frappe_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='hot_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='normal_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='special_price',
            field=models.FloatField(null=True),
        ),
    ]
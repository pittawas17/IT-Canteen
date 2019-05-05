# Generated by Django 2.2 on 2019-05-04 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0004_auto_20190504_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='Ingre_name',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.TextField(default='some ingredient', max_length=50),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_shop',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.PROTECT, to='ordering.Shop'),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_shop',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.PROTECT, to='ordering.Shop'),
        ),
    ]
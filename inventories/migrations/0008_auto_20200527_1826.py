# Generated by Django 3.0.6 on 2020-05-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0007_auto_20200525_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Additional Product Information.'),
        ),
    ]
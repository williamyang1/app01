# Generated by Django 4.1 on 2022-09-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_boss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boss',
            name='img',
            field=models.CharField(max_length=64, verbose_name='head'),
        ),
    ]
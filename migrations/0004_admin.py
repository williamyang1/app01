# Generated by Django 4.1 on 2022-09-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_prettynum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='user name')),
                ('password', models.CharField(max_length=64, verbose_name='pwd')),
            ],
        ),
    ]

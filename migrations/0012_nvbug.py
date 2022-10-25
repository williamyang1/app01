# Generated by Django 4.1 on 2022-09-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_alter_city_count_alter_city_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NvBug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BugId', models.IntegerField(verbose_name='BugID')),
                ('Synopsis', models.CharField(max_length=200, verbose_name='Synopsis')),
                ('BugAction', models.CharField(max_length=100, verbose_name='BugAction')),
                ('Module', models.CharField(max_length=100, verbose_name='Module')),
                ('Priority', models.CharField(max_length=100, verbose_name='Priority')),
                ('RequestDate', models.DateField(verbose_name='RequestDate')),
                ('Categories', models.CharField(max_length=100, verbose_name='Categories')),
                ('Disposition', models.CharField(max_length=100, verbose_name='Disposition')),
                ('QAEngineer', models.CharField(max_length=100, verbose_name='QAEngineer')),
                ('Engineer', models.CharField(max_length=200, verbose_name='Engineer')),
                ('CustomKeywords', models.CharField(max_length=200, verbose_name='CustomKeywords')),
                ('ModifiedDate', models.CharField(max_length=100, verbose_name='ModifiedDate')),
                ('Version', models.CharField(max_length=100, verbose_name='Version')),
                ('Origin', models.CharField(max_length=100, verbose_name='Origin')),
                ('Regression', models.CharField(max_length=50, verbose_name='Regression')),
                ('Error', models.TextField(verbose_name='Error')),
                ('Tlist', models.TextField(verbose_name='Tlist')),
                ('buglink', models.CharField(max_length=200, verbose_name='buglink')),
            ],
        ),
    ]
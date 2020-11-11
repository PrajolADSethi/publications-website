# Generated by Django 2.2.7 on 2020-11-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='college',
            name='clgID',
        ),
        migrations.RemoveField(
            model_name='department',
            name='deptID',
        ),
        migrations.AlterField(
            model_name='author',
            name='ORCid',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='scopusID',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='weblinks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-11-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_auto_20201123_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2020-11-12 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_auto_20201111_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_app.College'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-11-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_remove_paper_authorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='DOI',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='citation',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='paper',
            name='citations_google_scholar',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='citations_ieee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='citations_researchgate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='citations_scopus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='citations_webofscience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='publication_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='fields',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='publisher_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

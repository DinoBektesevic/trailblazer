# Generated by Django 3.1.7 on 2021-06-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20210623_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='filter',
        ),
        migrations.AddField(
            model_name='metadata',
            name='filter_name',
            field=models.CharField(max_length=30, null=True, verbose_name='filter name'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='processor_name',
            field=models.CharField(max_length=20, verbose_name='name of translator used to process FITS header information'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='standardizer_name',
            field=models.CharField(max_length=20, verbose_name='name of standardizer used to process FITS header information'),
        ),
    ]

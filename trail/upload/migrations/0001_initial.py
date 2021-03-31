# Generated by Django 3.1.7 on 2021-03-31 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.IntegerField()),
                ('camcol', models.IntegerField()),
                ('filter', models.CharField(max_length=1)),
                ('field', models.IntegerField()),
                ('ctype', models.CharField(max_length=20)),
                ('crpix1', models.FloatField()),
                ('crpix2', models.FloatField()),
                ('crval1', models.FloatField()),
                ('crval2', models.FloatField()),
                ('cd11', models.FloatField()),
                ('cd12', models.FloatField()),
                ('cd21', models.FloatField()),
                ('cd22', models.FloatField()),
                ('t', models.DateTimeField(verbose_name='UTC time at exposure start.')),
            ],
        ),
        migrations.AddConstraint(
            model_name='exampleframe',
            constraint=models.UniqueConstraint(fields=('run', 'camcol', 'filter', 'field'), name='SDSS unique identifiers.'),
        ),
    ]

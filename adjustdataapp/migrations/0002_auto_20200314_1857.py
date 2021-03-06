# Generated by Django 3.0.4 on 2020-03-14 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adjustdataapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='cpi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='created_date',
            field=models.DateField(auto_created=True, blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='dataset',
            name='updated_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='channel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='os',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterModelTable(
            name='dataset',
            table='performancematrics',
        ),
    ]

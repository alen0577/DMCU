# Generated by Django 4.0.2 on 2023-06-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0053_remove_daily_leeds_sub_remove_daily_leeds_sub_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_leads',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='daily_leeds',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]

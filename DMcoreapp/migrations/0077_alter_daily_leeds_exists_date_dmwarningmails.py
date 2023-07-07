# Generated by Django 4.1.4 on 2023-07-04 05:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0076_alter_daily_leeds_exists_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_leeds_exists',
            name='date',
            field=models.DateField(default=datetime.date(2023, 7, 4)),
        ),
        migrations.CreateModel(
            name='DMWarningMails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('executive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.user_registration')),
            ],
        ),
    ]
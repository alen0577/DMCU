# Generated by Django 4.1.7 on 2023-07-07 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0083_rename_warning_mail_work_mail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_leeds_exists',
            name='date',
            field=models.DateField(default=datetime.date(2023, 7, 7)),
        ),
    ]

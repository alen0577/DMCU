# Generated by Django 4.1.4 on 2023-07-06 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0082_work_warning_mail_alter_daily_leeds_exists_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='warning_mail',
            new_name='mail_status',
        ),
    ]

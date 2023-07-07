# Generated by Django 4.0.2 on 2023-05-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0040_smo_post_st_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='diry',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='diry_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='diry_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='fb',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='fb_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='fb_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='insta',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='insta_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='insta_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='link',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='link_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='link_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='pin',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='pin_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='pin_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='qra',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='qra_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='qra_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='sbms',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='sbms_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='sbms_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='st_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='tumb',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='tumb_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='tumb_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='tw',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='tw_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='tw_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
        migrations.AddField(
            model_name='events',
            name='yt',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='yt_dt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='yt_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/smo_post/'),
        ),
    ]
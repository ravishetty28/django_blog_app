# Generated by Django 3.1 on 2021-07-23 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210722_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='website_uel',
            new_name='website_url',
        ),
    ]

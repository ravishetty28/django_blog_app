# Generated by Django 3.1 on 2021-07-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click on the link to view the blog post', max_length=255),
        ),
    ]

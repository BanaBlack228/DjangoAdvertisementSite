# Generated by Django 5.2 on 2025-05-01 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, null=True, unique=True),
        ),
    ]

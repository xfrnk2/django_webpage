# Generated by Django 3.0.3 on 2020-04-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='공개여부'),
        ),
    ]
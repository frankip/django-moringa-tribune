# Generated by Django 4.0.4 on 2022-05-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]

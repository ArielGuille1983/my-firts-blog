# Generated by Django 2.2.19 on 2021-04-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
# Generated by Django 3.2.13 on 2022-05-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=80),
        ),
    ]
# Generated by Django 3.2.13 on 2022-05-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.IntegerField(default='0'),
        ),
    ]
# Generated by Django 3.2.13 on 2022-05-21 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_delete_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvote',
        ),
    ]
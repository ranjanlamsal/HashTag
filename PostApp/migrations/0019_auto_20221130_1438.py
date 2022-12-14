# Generated by Django 3.2.4 on 2022-11-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_userprofile_email'),
        ('PostApp', '0018_remove_post_no_of_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='post',
            name='downvote_users',
            field=models.ManyToManyField(blank=True, default=None, related_name='downvoted_by', to='User.UserProfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote_users',
            field=models.ManyToManyField(blank=True, default=None, related_name='upvoted_by', to='User.UserProfile'),
        ),
    ]

# Generated by Django 4.1 on 2022-11-05 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0006_alter_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]

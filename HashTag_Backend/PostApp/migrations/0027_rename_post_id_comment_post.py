# Generated by Django 3.2.4 on 2023-03-12 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0026_rename_post_comment_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
    ]
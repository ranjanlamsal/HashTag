# Generated by Django 3.2.4 on 2023-03-12 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_userprofile_email'),
        ('PostApp', '0024_rename_photo_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commented_on', to='PostApp.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to='User.userprofile'),
        ),
    ]

# Generated by Django 3.2.4 on 2022-11-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20221120_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='None@none.com', max_length=200),
            preserve_default=False,
        ),
    ]
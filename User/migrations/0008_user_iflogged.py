# Generated by Django 4.1 on 2022-09-08 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_user_photo_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ifLogged',
            field=models.BooleanField(default=False),
        ),
    ]
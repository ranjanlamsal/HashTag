# Generated by Django 4.1 on 2022-09-15 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0001_initial'),
        ('PostApp', '0002_alter_post_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='Tag.tag'),
        ),
    ]
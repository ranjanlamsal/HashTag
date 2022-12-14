# Generated by Django 4.1 on 2022-09-15 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('no_of_likes', models.IntegerField(default=0)),
                ('liked_by', models.ManyToManyField(blank=True, default=None, to='User.user')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='User.user')),
                ('tag', models.ManyToManyField(blank=True, to='Tag.tag')),
            ],
        ),
    ]

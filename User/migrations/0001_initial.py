# Generated by Django 4.1 on 2022-09-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('password2', models.CharField(max_length=128)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('ifLogged', models.BooleanField(default=False)),
                ('followed', models.ManyToManyField(default=None, related_name='followed', to='Tag.tag')),
            ],
        ),
    ]

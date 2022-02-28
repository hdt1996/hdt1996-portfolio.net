# Generated by Django 3.2.7 on 2022-02-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostSongData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=500, null=True)),
                ('time', models.DecimalField(decimal_places=2, max_digits=500, null=True)),
                ('image_url', models.CharField(max_length=500, null=True)),
                ('is_playing', models.BooleanField(default=False)),
                ('votes', models.IntegerField(default=0)),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpotifyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('refresh_token', models.CharField(max_length=500)),
                ('access_token', models.CharField(max_length=500)),
                ('expiration', models.DateTimeField()),
                ('token_type', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 2.1.5 on 2023-03-06 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('Movie_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=50)),
                ('Poster', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=200)),
                ('IMDB_Rating', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('rating_ID', models.AutoField(primary_key=True, serialize=False)),
                ('user_Rating', models.IntegerField(default=0)),
                ('movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('role', models.CharField(blank=True, max_length=20)),
                ('genres', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchedList',
            fields=[
                ('watchedList_ID', models.AutoField(primary_key=True, serialize=False)),
                ('movie_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.Movie')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.UserProfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='movie_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.Movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieflix.UserProfile'),
        ),
    ]

# Generated by Django 2.2.5 on 2021-12-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('favs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fav',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='fav_lists', to='movies.Movie'),
        ),
    ]
# Generated by Django 2.2.5 on 2021-11-30 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211130_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('Common', (('action', 'Action'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('mystery', 'Mystery'))), ('Movie', (('comedy', 'Comedy'), ('drama', 'Drama'), ('romance', 'Romance'), ('thriller', 'Thriller'))), ('Book', (('adventure', 'Adventure'), ('classics', 'Classics'), ('comicBook', 'Comic Book'), ('detective', 'Dectective'), ('historical', 'Historical Fiction'), ('literary', 'Literary Fiction')))], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='favouriteMovieGenre',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favouriteMovieGenre', to='users.Genre'),
        ),
    ]
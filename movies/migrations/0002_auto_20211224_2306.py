# Generated by Django 2.2.5 on 2021-12-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(blank=True, to='people.Person'),
        ),
    ]

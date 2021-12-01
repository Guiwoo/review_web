# Generated by Django 2.2.5 on 2021-12-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='Unknown', max_length=20)),
                ('sort', models.CharField(choices=[('actor', 'Actor'), ('actress', 'Actress'), ('director', 'Director'), ('writer', 'Writer')], max_length=9)),
                ('photo', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

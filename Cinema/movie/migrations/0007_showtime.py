# Generated by Django 3.2 on 2021-05-01 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_moviepost_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.moviepost')),
            ],
        ),
    ]
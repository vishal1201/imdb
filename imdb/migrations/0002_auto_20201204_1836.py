# Generated by Django 3.1.4 on 2020-12-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='genre_name',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='movie',
        ),
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='imdb.Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(default=0.0, verbose_name='99 popularity'),
        ),
    ]
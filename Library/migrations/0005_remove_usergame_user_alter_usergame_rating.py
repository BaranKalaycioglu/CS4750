# Generated by Django 4.1 on 2023-06-29 00:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_usergame_playtime_alter_usergame_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergame',
            name='user',
        ),
        migrations.AlterField(
            model_name='usergame',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
# Generated by Django 3.1.4 on 2021-02-13 23:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0018_auto_20210213_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

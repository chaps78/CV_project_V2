# Generated by Django 3.1.4 on 2021-02-01 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0006_auto_20210201_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='niveaux',
            name='text',
        ),
        migrations.AddField(
            model_name='competences',
            name='text',
            field=models.TextField(default=' '),
        ),
    ]

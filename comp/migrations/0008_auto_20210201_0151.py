# Generated by Django 3.1.4 on 2021-02-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0007_auto_20210201_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competences',
            name='text',
        ),
        migrations.AlterField(
            model_name='competences',
            name='detail',
            field=models.TextField(default=' '),
        ),
    ]

# Generated by Django 3.1.4 on 2021-02-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0010_experiences_detail_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='competences',
            name='detail_en',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='experiences',
            name='intitule_en',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
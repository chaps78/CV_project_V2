# Generated by Django 3.1.4 on 2021-01-03 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_niveaux_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiences',
            old_name='competences',
            new_name='compet',
        ),
    ]

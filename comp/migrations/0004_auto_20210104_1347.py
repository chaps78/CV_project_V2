# Generated by Django 3.1.4 on 2021-01-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0003_auto_20210103_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiences',
            name='logo_client',
            field=models.CharField(max_length=200),
        ),
    ]

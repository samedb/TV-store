# Generated by Django 3.0.6 on 2020-05-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVStore_API', '0009_naruceniartikl_porudzbina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porudzbina',
            name='datumPorudzbine',
            field=models.CharField(max_length=20),
        ),
    ]
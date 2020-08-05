# Generated by Django 3.0.8 on 2020-08-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVStore_API', '0010_auto_20200517_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='porudzbina',
            name='ukupna_cena',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='naruceniartikl',
            name='kolicina',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='porudzbina',
            name='zavrsenaPoruzbina',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tv',
            name='boja',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='ekran',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='energetski_razred',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='tv',
            name='masa',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='model',
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='proizvodjac',
            field=models.CharField(max_length=63),
        ),
        migrations.AlterField(
            model_name='tv',
            name='rezolucija',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tv',
            name='smart',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='tip_tunera',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='vesa',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='wireless',
            field=models.CharField(blank=True, max_length=127),
        ),
        migrations.AlterField(
            model_name='tv',
            name='zvucnici',
            field=models.CharField(blank=True, max_length=127),
        ),
    ]
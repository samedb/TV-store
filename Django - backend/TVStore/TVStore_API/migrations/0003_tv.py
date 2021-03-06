# Generated by Django 3.0.6 on 2020-05-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVStore_API', '0002_auto_20200515_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='TV',
            fields=[
                ('ean', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cena', models.IntegerField()),
                ('cena_na_popustu', models.IntegerField()),
                ('dostupno', models.BooleanField()),
                ('proizvodjac', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('dijagonala', models.IntegerField()),
                ('rezolucija', models.CharField(max_length=30)),
                ('smart', models.CharField(max_length=5)),
                ('ekran', models.CharField(max_length=20)),
                ('tip_tunera', models.CharField(max_length=20)),
                ('energetski_razred', models.CharField(max_length=5)),
                ('wireless', models.CharField(max_length=10)),
                ('povezivanje', models.CharField(max_length=50)),
                ('vesa', models.CharField(max_length=20)),
                ('boja', models.CharField(max_length=20)),
                ('dvb_c', models.CharField(default='Ne', max_length=5)),
                ('dvb_s2', models.CharField(default='Ne', max_length=5)),
                ('dvb_t2', models.CharField(default='Ne', max_length=5)),
                ('zvucnici', models.CharField(max_length=20)),
                ('masa', models.CharField(max_length=20)),
                ('dimenzije', models.CharField(max_length=50)),
                ('dodatne_prednosti', models.CharField(max_length=500)),
                ('slike', models.CharField(max_length=1000)),
            ],
        ),
    ]

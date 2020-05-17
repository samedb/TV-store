# Generated by Django 3.0.6 on 2020-05-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVStore_API', '0004_auto_20200515_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv',
            name='ostalo',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tv',
            name='cena',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tv',
            name='dijagonala',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tv',
            name='dimenzije',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tv',
            name='povezivanje',
            field=models.CharField(max_length=500),
        ),
    ]

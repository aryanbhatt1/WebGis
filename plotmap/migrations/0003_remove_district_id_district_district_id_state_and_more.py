# Generated by Django 4.0.3 on 2022-03-31 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotmap', '0002_district_id_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='id_district',
        ),
        migrations.AddField(
            model_name='district',
            name='id_state',
            field=models.IntegerField(null=True, verbose_name='State ID'),
        ),
        migrations.AddField(
            model_name='itemcode',
            name='id_district',
            field=models.IntegerField(null=True, verbose_name='District ID'),
        ),
    ]

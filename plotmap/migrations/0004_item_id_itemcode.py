# Generated by Django 4.0.3 on 2022-03-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plotmap', '0003_remove_district_id_district_district_id_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='id_itemcode',
            field=models.IntegerField(null=True, verbose_name='Item Code'),
        ),
    ]

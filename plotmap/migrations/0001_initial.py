# Generated by Django 4.0.3 on 2022-03-31 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemCode', models.IntegerField(null=True, verbose_name='Item Code')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='State')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=50, null=True, verbose_name='Item')),
                ('ItemCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plotmap.itemcode')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=50, null=True, verbose_name='District')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plotmap.state')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=30, null=True)),
                ('departmentName', models.CharField(max_length=100, null=True, verbose_name='Department Name')),
                ('departmentAddress', models.CharField(max_length=100, null=True, verbose_name='Department Address')),
                ('contactperson', models.CharField(max_length=100, null=True, verbose_name='Contact Person')),
                ('contactno', models.CharField(max_length=20, null=True, verbose_name='Contact No')),
                ('contactEmail', models.EmailField(max_length=254, null=True, verbose_name='Contact Email')),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plotmap.item')),
                ('ItemCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plotmap.itemcode')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plotmap.district')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plotmap.state')),
            ],
        ),
    ]

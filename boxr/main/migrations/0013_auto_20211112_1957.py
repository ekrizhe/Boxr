# Generated by Django 3.2.3 on 2021-11-13 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_merge_0011_location_0011_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='pallet',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.pallets'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]

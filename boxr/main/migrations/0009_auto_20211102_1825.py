# Generated by Django 3.2.3 on 2021-11-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_merge_20211028_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='pallets',
            name='location',
            field=models.CharField(default='Floor', max_length=50),
        ),
        migrations.AlterField(
            model_name='carton_qty',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pallets',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='products_on_pallets',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

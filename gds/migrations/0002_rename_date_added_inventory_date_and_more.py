# Generated by Django 5.0 on 2023-12-17 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='date_added',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='item_name',
            new_name='ItemName',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='current_stock_pile',
            new_name='StockPile',
        ),
    ]

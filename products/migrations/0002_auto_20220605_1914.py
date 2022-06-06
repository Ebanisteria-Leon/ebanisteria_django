# Generated by Django 3.2.9 on 2022-06-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproducto',
            name='destacado',
            field=models.CharField(default='', max_length=30, verbose_name='Tipo del Producto'),
        ),
        migrations.AddField(
            model_name='historicalproducto',
            name='tiempoProducto',
            field=models.CharField(default='', max_length=30, verbose_name='Tiempo del Producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='destacado',
            field=models.CharField(default='', max_length=30, verbose_name='Tipo del Producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tiempoProducto',
            field=models.CharField(default='', max_length=30, verbose_name='Tiempo del Producto'),
        ),
        migrations.AlterField(
            model_name='historicalproducto',
            name='estadoProducto',
            field=models.CharField(default='', max_length=30, verbose_name='Estado del Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estadoProducto',
            field=models.CharField(default='', max_length=30, verbose_name='Estado del Producto'),
        ),
    ]

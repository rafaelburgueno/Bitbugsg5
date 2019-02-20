# Generated by Django 2.1.5 on 2019-02-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_auto_20190219_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='fecha_despachable',
            field=models.CharField(blank=True, default='0000', max_length=100, verbose_name='Fecha despachable'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='fecha_despacho',
            field=models.CharField(blank=True, default='0000', max_length=100, verbose_name='Fecha de despacho'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='fecha_procesamiento',
            field=models.CharField(blank=True, default='0000', max_length=100, verbose_name='Fecha de procesamiento'),
        ),
    ]
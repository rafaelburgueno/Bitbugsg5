# Generated by Django 2.1.5 on 2019-02-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20190218_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='cama',
            field=models.CharField(max_length=100, verbose_name='Cama'),
        ),
    ]

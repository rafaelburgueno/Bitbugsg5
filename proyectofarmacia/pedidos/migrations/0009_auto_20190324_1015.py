# Generated by Django 2.1.5 on 2019-03-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_auto_20190220_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='created',
            field=models.CharField(blank=True, default='24/03/2019 10:15:25', max_length=100, verbose_name='Fecha de creación'),
        ),
    ]

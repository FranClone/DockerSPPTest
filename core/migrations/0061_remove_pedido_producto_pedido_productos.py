# Generated by Django 4.1.8 on 2023-07-20 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_pedido_linea_produccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(blank=True, to='core.producto'),
        ),
    ]
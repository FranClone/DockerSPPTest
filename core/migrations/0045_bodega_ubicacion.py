# Generated by Django 4.1.7 on 2023-05-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_remove_producto_ancho_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodega',
            name='ubicacion',
            field=models.CharField(default='Concepcion', max_length=20),
            preserve_default=False,
        ),
    ]

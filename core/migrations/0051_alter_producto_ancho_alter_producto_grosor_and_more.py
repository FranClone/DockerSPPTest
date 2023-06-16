# Generated by Django 4.1.8 on 2023-06-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_materiaprima_alter_producto_ancho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ancho',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='producto',
            name='grosor',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='producto',
            name='largo',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
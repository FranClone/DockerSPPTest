# Generated by Django 4.1.8 on 2023-07-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_rename_codigo_patron_patroncorte_codigo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='grosor',
            new_name='alto',
        ),
        migrations.AddField(
            model_name='producto',
            name='costo_almacenamiento',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='demanda',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='inventario_final',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='inventario_inicial',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='valor_inventario',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='volumen_obtenido',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]

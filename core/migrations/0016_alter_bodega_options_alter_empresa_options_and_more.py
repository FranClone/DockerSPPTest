# Generated by Django 4.1.6 on 2023-02-24 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_bodega_options_alter_detallepedido_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodega',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='empresa',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'managed': False},
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='id_pedido',
            field=models.ForeignKey(blank=True, db_column='id_pedido', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.pedido'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='id_producto',
            field=models.ForeignKey(blank=True, db_column='id_producto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.producto'),
        ),
        migrations.AddField(
            model_name='linea',
            name='rut_empresa',
            field=models.ForeignKey(blank=True, db_column='rut_empresa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.empresa'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='rut_empresa',
            field=models.ForeignKey(blank=True, db_column='rut_empresa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.empresa'),
        ),
    ]

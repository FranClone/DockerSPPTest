# Generated by Django 4.1.7 on 2023-04-21 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_cliente_empresa_alter_cliente_nombre_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='ClienteEmpresa',
        ),
    ]

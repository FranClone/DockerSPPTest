# Generated by Django 4.1.7 on 2023-04-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_remove_clienteempresa_cliente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_cliente', models.CharField(max_length=20)),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='Cliente')),
                ('correo_cliente', models.CharField(blank=True, max_length=300, null=True)),
                ('estado_cliente', models.BooleanField(blank=True, null=True)),
                ('fecha_vigencia', models.DateField(blank=True, null=True)),
                ('fecha_crea', models.DateField(auto_now_add=True)),
                ('usuario_crea', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre_fantasia', models.CharField(blank=True, max_length=100, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'CLIENTE',
            },
        ),
    ]

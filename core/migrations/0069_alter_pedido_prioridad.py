# Generated by Django 4.2.4 on 2023-08-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_alter_patroncorte_rendimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='prioridad',
            field=models.CharField(max_length=20),
        ),
    ]

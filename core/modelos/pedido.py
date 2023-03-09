# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    numero_pedido = models.CharField(max_length=200, verbose_name='Número de Pedido', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    destino_pedido = models.CharField(max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    rut_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name='Empresa', db_column='rut_empresa', blank=True, null=True)
    usuario_crea = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fecha_crea = models.DateField(auto_now_add=True, blank=True, null=True)
    estado_pedido = models.IntegerField(blank=True, null=True)
    PRIORIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    prioridad = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', choices=PRIORIDAD_CHOICES, blank=True, null=True)

    class Meta:
        db_table = 'PEDIDO'

    def __str__(self):
        return 'Número de Pedido: ' + self.numero_pedido
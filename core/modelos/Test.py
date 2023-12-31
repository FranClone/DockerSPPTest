# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserProfile(models.Model):
    rut = models.CharField(primary_key=True, max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    rut_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='rut_empresa')

    class Meta:
        managed = False
        db_table = 'USER_PROFILE'

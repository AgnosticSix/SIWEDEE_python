from django.db import models

# Create your models here.

class ASIGNA_EMPRESA(models.Model):
    IDASIGNA = models.AutoField(primary_key=True)
    IDEMPRESA = models.IntegerField(null=True)
    IDALUMNO = models.IntegerField(null=True)
    FECHA_VINCU = models.DateField(null=False)
    FECHA_CAMBIO = models.DateField(null=True)

class CATALUMNO(models.Model):
	IDALUMNO = models.AutoField(primary_key=True)
	MATRICULA = models.IntegerField(null=False)
	IDPROCESO = models.IntegerField(null=True)
	IDCARRERA = models.IntegerField(null=True)
	IDEMPRESA = models.IntegerField(null=True)
	ACTIVO = models.BooleanField(null=False)

class CATCALIFICACIONES(models.Model):
	IDCALIF = models.AutoField(primary_key=True)
	IDALUMNO = models.IntegerField(null=False)
	CAL_AA  =  models.IntegerField(null=False)
	CAL_AL = models.IntegerField(null=False)

class CATCARRERAS(models.Model):
	IDCARREA = models.AutoField(primary_key=True)
	DESCRIPCION = models.CharField(max_length=50, null=False)
	ABREVIATURA = models.CharField(max_length=12, null=False)

class CATEMPRESAS(models.Model):
	IDEMPRESA = models.AutoField(primary_key=True)
	NOMBRE = models.CharField(max_length=50, null=False)
	REPRESENTANTE = models.CharField(max_length=100, null=True)
	TELEFONO = models.BigIntegerField(null=False)
	DOMICILIO = models.CharField(max_length=120, null=False)
	EMAIL = models.EmailField(null=False)
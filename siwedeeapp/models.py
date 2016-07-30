from django.db import models

# Create your models here.

<<<<<<< HEAD
class CATALUMNO(models.Model):
	IDALUMNO = models.AutoField(primary_key=True)
=======
class ASIGNA_EMPRESA(models.Model):
    IDASIGNA = models.AutoField(primary_key=True)
    IDEMPRESA = models.ForeignKey(CATEMPRESAS)
    IDALUMNO = models.ForeignKey(CATALUMNOS)
    FECHA_VINCU = models.DateField(null=False)
    FECHA_CAMBIO = models.DateField(null=True)

class CATALUMNOS(models.Model):
	IDALUMNO = models.ForeignKey(CATALUMNOS)
>>>>>>> 93048d8325bef80598ba6ebf3e9b449230a3d949
	MATRICULA = models.IntegerField(null=False)
	IDPROCESO = models.ForeignKey(PROCESO)
	IDCARRERA = models.ForeignKey(CATCARRERAS)
	IDEMPRESA = models.ForeignKey(CATEMPRESAS ,null=True)
	ACTIVO = models.BooleanField(null=False)

	def __str__(self):
		return self.IDALUMNO

class CATCALIFICACIONES(models.Model):
	IDCALIF = models.AutoField(primary_key=True)
	IDALUMNO = models.ForeignKey(CATALUMNO)
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

	def __str__(self):
		return self.IDEMPRESA

class CATHISTREP(models.Model):
	IDALUMNO = models.ForeignKey(CATALUMNOS)
	FECHA_SUBIDA = models.DateField(null=False)
	TIPO_REP = models.CharField(max_length=15, null=False)

class CATMAESTROS(models.Model):
	IDMAESTRO = models.AutoField(primary_key=True)
	IDPERSONA = models.ForeignKey(CATPERSONAS)

class CATPERSONAS(models.Model):
	IDPERSONA = models.AutoField(primary_key=True)
	IDTIPOPERSONA = models.ForeignKey(TIPOPERSONA)
	NOMBRE= models.CharField(max_length=50, null=False)
	APELLIDO_PAT = models.CharField(max_length=50, null=False)
	APELLIDO_MAT = models.CharField(max_length=50, null=True)
	SEXO = models.CharField(max_length=1, null=False)
	USUARIO = models.CharField(max_length=30, null=False)
	PASSWORD = models.CharField(max_length=30, null=False)
	ACTIVO = models.BooleanField(null=False)

class PERIODOESCOLAR(models.Model):
	IDPERIODO = models.AutoField(primary_key=True)
	NOMBRE = models.CharField(max_length=50, null=False)
	FECHA_INI = models.DateField(null=False)
	FECHA_FIN = models.DateField(null=False)

class PROCESO(models.Model):
	IDPROCESO = models.AutoField(primary_key=True)
	ID_PERIODO = models.ForeignKey(PERIODOESCOLAR)
	NOMBRE = models.CharField(max_length=25)

class ASIGNA_EMPRESA(models.Model):
    IDASIGNA = models.AutoField(primary_key=True)
    IDEMPRESA = models.ForeignKey(CATEMPRESAS)
    IDALUMNO = models.ForeignKey(CATALUMNO)
    FECHA_VINCU = models.DateField(null=False)
    FECHA_CAMBIO = models.DateField(null=True)

class TIPOPERSONA(models.Model):
	IDTIPOPERSONA = models.AutoField(primary_key=True)
	NOMBRE = models.CharField(max_length=30, null=False)
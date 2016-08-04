from django.db import models

# Create your models here.

class ESTATUS(models.Model):
	IDESTATUS = models.AutoField(primary_key=True)
	DESCRIPCION = models.CharField(max_length=50)

	def __str__(self):
		return '%s %s'%(str(self.IDESTATUS), self.DESCRIPCION)

class PERIODOESCOLAR(models.Model):
	IDPERIODO = models.AutoField(primary_key=True)
	NOMBRE = models.CharField(max_length=50, null=False)
	FECHA_INI = models.DateField(null=False)
	FECHA_FIN = models.DateField(null=False)

	def __str__(self):
		return '%s %s'%(str(self.IDPERIODO), self.NOMBRE)

class PROCESO(models.Model):
	IDPROCESO = models.AutoField(primary_key=True)
	ID_PERIODO = models.ForeignKey(PERIODOESCOLAR)
	NOMBRE = models.CharField(max_length=30)

	def __str__(self):
		return '%s %s'%(str(self.IDPROCESO), self.NOMBRE)

class CATCARRERAS(models.Model):
	IDCARRERA = models.AutoField(primary_key=True)
	DESCRIPCION = models.CharField(max_length=50, null=False)
	ABREVIATURA = models.CharField(max_length=12, null=False)

	def __str__(self):
		return '%s %s'%(str(self.IDCARRERA), self.ABREVIATURA)

class CATEMPRESAS(models.Model):
	IDEMPRESA = models.AutoField(primary_key=True)
	NOMBRE = models.CharField(max_length=50, null=False)
	REPRESENTANTE = models.CharField(max_length=100, null=True)
	TELEFONO = models.BigIntegerField(null=False)
	DOMICILIO = models.CharField(max_length=120, null=False)
	EMAIL = models.EmailField(null=False)

	def __str__(self):
		return '%s %s'%(str(self.IDEMPRESA), self.NOMBRE)

class TIPOPERSONA(models.Model):
	IDTIPOPERSONA = models.AutoField(primary_key=True)
	NOMBRE = models.CharField(max_length=30, null=False)

	def __str__(self):
		return '%s %s'%(str(self.IDTIPOPERSONA), self.NOMBRE)

class CATALUMNOS(models.Model):
	IDALUMNO = models.ForeignKey(IDPERSONA, primary_key=True)
	MATRICULA = models.CharField(max_length=6, null=False)
	IDPROCESO = models.ForeignKey(PROCESO)
	IDCARRERA = models.ForeignKey(CATCARRERAS)
	IDEMPRESA = models.ForeignKey(CATEMPRESAS)
	IDESTATUS = models.ForeignKey(ESTATUS)
	ACTIVO = models.BooleanField(null=False)

	def __str__(self):
		return '%s %s'%(str(self.IDALUMNO), self.MATRICULA)

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

	def __str__(self):
		return '%s %s'%(str(self.IDPERSONA), self.NOMBRE)

class CATCALIFICACIONES(models.Model):
	IDCALIF = models.AutoField(primary_key=True)
	IDALUMNO = models.ForeignKey(CATALUMNOS)
	CAL_AA  =  models.IntegerField(null=False)
	CAL_AL = models.IntegerField(null=False)

	def __str__(self):
		return '%s %s'%(str(self.IDALUMNO), self.IDCALIF)

class CATHISTREP(models.Model):
	IDALUMNO = models.ForeignKey(CATALUMNOS)
	FECHA_SUBIDA = models.DateField(null=False)
	TIPO_REP = models.CharField(max_length=20, null=False)


class CATMAESTROS(models.Model):
	IDMAESTRO = models.AutoField(primary_key=True)
	IDPERSONA = models.ForeignKey(CATPERSONAS)

	def __str__(self):
		return '%s %s'%(str(self.IDMAESTRO), self.IDPERSONA)

class ASIGNA_EMPRESA(models.Model):
	IDASIGNA = models.AutoField(primary_key=True)
	IDEMPRESA = models.ForeignKey(CATEMPRESAS)
	IDALUMNO = models.ForeignKey(CATALUMNOS)
	FECHA_VINCU = models.DateField(null=False)
	FECHA_CAMBIO = models.DateField(null=True)

	def __str__(self):
		return '%s %s'%(str(self.IDASIGNA), self.IDEMPRESA)

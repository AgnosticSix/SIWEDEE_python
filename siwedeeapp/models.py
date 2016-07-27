from django.db import models

# Create your models here.
class ID_ASIGNA(models.Model):
    idasigna = models.IntegerField()

    def __str__(self):
        return self.idasigna

class ID_ALUMNO(models.Model):
	idalumno = models.IntegerField()

	def __str__(self):
		return self.idalumno

class ID_CALIF(models.Model):
	idcalif = models.IntegerField()

	def __str__(self):
		return self.idcalif

class ID_CARRERA(models.Model):
	idcarrera = models.IntegerField()

	def __str__(self):
	 	return self.idcarrera

class ID_EMPRESA(models.Model):
	idempresa = models.IntegerField()

	def __str__(self):
		return self.idempresa 

class ASIGNA_EMPRESA(models.Model):
    IDASIGNA = models.ForeignKey(ID_ASIGNA, null=False)
    IDEMPRESA = models.IntegerField(null=True)
    IDALUMNO = models.IntegerField(null=True)
    FECHA_VINCU = models.DateField(null=False)
    FECHA_CAMBIO = models.DateField(null=True)

class CATALUMNO(models.Model):
	IDALUMNO = models.ForeignKey(ID_ALUMNO, null=False)
	MATRICULA = models.IntegerField(null=False)
	IDPROCESO = models.IntegerField(null=True)
	IDCARRERA = models.IntegerField(null=True)
	IDEMPRESA = models.IntegerField(null=True)
	ACTIVO = models.BooleanField(null=False)

class CATCALIFICACIONES(models.Model):
	IDCALIF = models.ForeignKey(ID_CALIF, null=False)
	IDALUMNO = models.IntegerField(null=False)
	CAL_AA  =  models.IntegerField(null=False)
	CAL_AL = models.IntegerField(null=False)

class CATCARRERAS(models.Model):
	IDCARREA = models.ForeignKey(ID_CARRERA, null=False)
	DESCRIPCION = models.CharField(max_length=50, null=False)
	ABREVIATURA = models.CharField(max_length=12, null=False)

class CATEMPRESAS(models.Model):
	IDEMPRESA = models.ForeignKey(ID_EMPRESA, null=False)
	NOMBRE = models.CharField(max_length=50, null=False)
	REPRESENTANTE = models.CharField(max_length=100, null=True)
	TELEFONO = models.BigIntegerField(null=False)
	DOMICILIO = models.CharField(max_length=120, null=False)
	EMAIL = models.EmailField(null=False)
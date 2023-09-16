from django.db import models

# Create your models here.
class Formulario(models.Model):
    idalumo = models.AutoField(primary_key=True, null=False)
    ci = models.IntegerField(unique=True)
    filiar = models.CharField(max_length=50)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    militancia = models.CharField(max_length=4, default=False)
    cargo = models.CharField(max_length=20, default=False)
    grado = models.CharField(max_length=20)
    carrera = models.CharField(max_length=30)
    masculino = models.BooleanField("Masculino", default=False)
    femenino = models.BooleanField("Femenina", default=False)
    teznegro = models.BooleanField("Negro",default=False)
    tezblanco = models.BooleanField("Blanco", default=False)
    tezmestizo = models.BooleanField("Mestizo", default=False)
    direccion = models.CharField(max_length=100)
    municipio = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    unidad = models.CharField(max_length=20)
    telefono = models.IntegerField()
    telefono_movil = models.IntegerField()
    fecha = models.DateTimeField()
    matricula = models.BooleanField("Matricula", default=False)
    rematricula = models.BooleanField("Rematricula", default=False)
    baja = models.BooleanField("Baja", default=False)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.ci)
        



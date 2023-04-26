from django.db import models

class Caneca(models.Model):
    codigo = models.AutoField(primary_key=True)
    ancho = models.DecimalField(max_digits=5, decimal_places=2)
    alto = models.DecimalField(max_digits=5, decimal_places=2)

class Colegio(models.Model):
    nit = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    contacto = models.CharField(max_length=100)
    fecha=models.DateField()

class Operario(models.Model):
    documento = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

class Recoleccion(models.Model):
    operario = models.ForeignKey(Operario, on_delete=models.CASCADE)
    caneca = models.ForeignKey(Caneca, on_delete=models.CASCADE)
    colegio =  models.ForeignKey(Colegio, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    preciokilo = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()


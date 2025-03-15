from django.shortcuts import render

# Create your views here.
class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True) 

class Cliente(models.Model): 
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50) 
    nacimiento = models.DateField(max_length=50, null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)
    
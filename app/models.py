"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)

 
class Candidatos(models.Model):
    nome = models.CharField(max_lenght=200)
    rg = models.CharField(max_lenght=50)
    cpf = models.CharField(max_lenght=50)
    endereco = models.CharField(max_lenght=200)
    telefone = models.CharField(max_lenght=200)


 class Locais Provas(models.Model):
    nome = models.CharField(max_lenght=200)
    endereco = models.CharField(max_lenght=200)
    cidade = models.CharField(max_lenght=200)
    estado = models.CharField(max_lenght=200)
  

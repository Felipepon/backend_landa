from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    cc = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='documentos/')
    subido_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
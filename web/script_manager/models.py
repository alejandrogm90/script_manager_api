from django.db import models


class Script(models.Model):
    nombre = models.CharField(max_length=300)
    comandos = models.CharField(max_length=400)
    resultado = models.TextField()
    inicio = models.DateTimeField(auto_now_add=True)  # Momento de inicio
    fin = models.DateTimeField(auto_now=True)  # Momento de fin; se actualiza automáticamente

    def __str__(self):
        return f'{self.nombre} | {self.comandos} | {str(self.resultado)} | {str(self.inicio)} | {str(self.fin)}'

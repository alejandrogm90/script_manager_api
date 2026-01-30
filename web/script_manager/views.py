import subprocess
import os
from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Script
from .serializers import ScriptSerializer


def index(request):
    scripts = Script.objects.order_by('-inicio')[:5]  # Obtener los últimos 5 scripts
    return render(request, 'script_manager/index.html', {'scripts': scripts})

class ScriptViewSet(viewsets.ViewSet):
    def create(self, request):
        script_name = request.data.get('script_name')
        parameters = request.data.get('parameters', '')  # Obtener parámetros, default a vacío
        script_path = os.path.join('scripts', script_name)

        # Capturar el momento de inicio
        inicio = datetime.now()

        try:
            # Ejecutar el script con parámetros
            comandos = ['python3', script_path] + parameters.split()  # Convertir a lista
            resultado = subprocess.run(comandos, capture_output=True, text=True)

            # Capturar el momento de fin
            fin = datetime.now()

            # Guardar resultado y tiempos en la base de datos
            script = Script(nombre=script_name, comandos=parameters, resultado=resultado.stdout, inicio=inicio, fin=fin)
            script.save()

            # Json salida
            salida = {'output': resultado.stdout, 'error': resultado.stderr, 'inicio': inicio, 'fin': fin }

            return Response(salida, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


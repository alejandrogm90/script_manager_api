import subprocess
import os
from datetime import datetime
from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Script
from .serializers import ScriptSerializer


def index(request):
    scripts = Script.objects.order_by('-inicio')[:5]  # Obtener los últimos 5 scripts
    return render(request, 'script_manager/index.html', {'scripts': scripts})

@extend_schema_view(
    list=extend_schema(description='Get a list of last 5 scripts launched')
)
class ScriptViewList(viewsets.ViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer

    def list(self, request):
        # Obtener los últimos 5 scripts
        scripts = Script.objects.order_by('-inicio')[:5]  # Ordenar por la fecha de inicio en orden descendente
        serializer = self.serializer_class(scripts, many=True)  # Usar el serializer para convertir a JSON
        return Response({"last_5": serializer.data}, status=200)

@extend_schema_view(
    #list=extend_schema(description='Get a list of last 5 scripts launched'),
    #retrieve=extend_schema(description='Get details of a specific category'),
    create=extend_schema(description='Create a new script execution'),
    #update=extend_schema(description='Update an existing category'),
    #destroy=extend_schema(description='Delete a category')
)
class ScriptViewSet(viewsets.ViewSet):
    queryset = Script.objects.all()
    serializer_class = ScriptSerializer

    def create(self, request):
        script_name = request.data.get('nombre')
        parameters = request.data.get('comandos', '')  # Obtener parámetros, default a vacío
        script_path = os.path.join('script_manager/scripts', script_name)

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
            salida = {'output': resultado.stdout, 'error': resultado.stderr, 'inicio': inicio, 'fin': fin}

            return Response(salida, status=201)
        except subprocess.CalledProcessError as e:
            return Response({'error': f'Error al ejecutar el script: {e.stderr}'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

import subprocess
import os
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Script
from .serializers import ScriptSerializer

class ScriptViewSet(viewsets.ViewSet):
    def create(self, request):
        script_name = request.data.get('script_name')
        script_path = os.path.join('scripts', script_name)  # Usar la ruta relativa

        try:
            # Ejecuta el script
            resultado = subprocess.run(['python3', script_path], capture_output=True, text=True)
            # Guardar resultado en la base de datos (opcional)
            script = Script(nombre=script_name, resultado=resultado.stdout)
            script.save()

            return Response({'output': resultado.stdout, 'error': resultado.stderr}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

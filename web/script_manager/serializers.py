from rest_framework import serializers
from .models import Script


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('nombre', 'comandos')

class FullScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('nombre', 'comandos', 'resultado', 'inicio', 'fin')

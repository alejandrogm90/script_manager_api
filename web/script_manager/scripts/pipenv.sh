#!/bin/bash

# Variables
file_name=$(basename "$1")     # Obtener el nombre del fichero
directory_path=$(dirname "$1") # Obtener el directorio

# Cambia al directorio especificado
cd "$directory_path" || { echo "Error: No se pudo cambiar al directorio"; exit 1; }

# Actualizar pipenv
pipenv update > /dev/null 2> /dev/null

# Ejecuta el script de Python
if pipenv run python "$file_name" "$@"; then
    echo "Script ejecutado correctamente"
else
    echo "Error: El script $file_name falló"
    exit 2
fi

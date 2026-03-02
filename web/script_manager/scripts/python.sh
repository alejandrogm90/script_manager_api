#!/bin/bash

# Variables
file_name=$(basename "$1")     # Obtener el nombre del fichero
directory_path=$(dirname "$1") # Obtener el directorio

# Cambia al directorio especificado
cd "$directory_path" || { echo "Error: No se pudo cambiar al directorio"; exit 1; }

# Ejecuta el script de Python
if python "$file_name" "$@"; then
    echo "Script ejecutado correctamente"
else
    echo "Error: El script $file_name falló"
    exit 2
fi

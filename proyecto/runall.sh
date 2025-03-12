#!/bin/bash

ENV_NAME="proyecto_investigacion"

if ! command -v conda &> /dev/null
then
    echo "Conda no está instalado. Por favor, instala Miniconda o Anaconda."
    exit 1
fi

if ! conda env list | grep -q "$ENV_NAME"; then
    echo "Creando el entorno Conda..."
    conda env create -f environment.yml
fi

echo "Activando el entorno Conda..."
source activate "$ENV_NAME"

if [ $? -ne 0 ]; then
    echo "No se pudo activar el entorno Conda."
    exit 1
fi

# Ejecutar el script principal
echo "Ejecutando el script principal..."
python main.py

echo "Desactivando el entorno Conda..."
conda deactivate

echo "Proceso completado."
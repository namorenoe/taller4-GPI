# Este archivo genera gráficos de los resultados

import matplotlib.pyplot as plt
import pandas as pd
import os

# Funcion para graficar los datos usando matplotlib.pyplot
# Param: df (data frame)
def graficar_resultados(df):
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.hist(df[column], bins=15, alpha=0.5, label=column)
    plt.title('Distribución de Datos Simulados')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.savefig('resultados/grafico_resultados.png')
    plt.close()
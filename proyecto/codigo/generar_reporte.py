# Este archivo genera un reporte final

import pandas as pd
import os

# Funcion para convertir a tablar los datos 
# Param: df (data frame)
def generar_reporte(df):
    df.to_csv('resultados/tabla_resultados.csv', index=False)
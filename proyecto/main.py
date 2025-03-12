import os
from datos.limpiar_datos import simular_datos
from codigo.analizar_datos import analizar_datos
from codigo.graficar_resultados import graficar_resultados
from codigo.generar_reporte import generar_reporte

if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Simular datos
df = simular_datos()

# Analizar datos
analisis = analizar_datos(df)
print(analisis)

# Generar gráfico
graficar_resultados(df)

# Generar reporte
generar_reporte(df)

print("Proceso completado. Resultados guardados en la carpeta 'resultados'.")
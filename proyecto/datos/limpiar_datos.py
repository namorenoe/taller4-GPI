# Este archivo limpia los datos

import urllib.request
import json
import numpy as np
import pandas as pd
from io import StringIO


# Funcion para simular datos usando numpy
def simular_datos(doi):

    record_id = doi.split('.')[-1]
    
    url = f"https://zenodo.org/api/records/{record_id}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            metadata = json.loads(data)
    except urllib.error.URLError as e:
        raise Exception(f"Error al acceder a Zenodo: {e.reason}")
    
    files = metadata.get('files', [])
    csv_file_url = None
    
    for file in files:
        if file['key'].endswith('.csv'): 
            csv_file_url = file['links']['self']
            break
    
    try:
        with urllib.request.urlopen(csv_file_url) as response:
            csv_data = response.read().decode('utf-8') 
    
    except urllib.error.URLError as e:
        raise Exception(f"Error al descargar el archivo CSV: {e.reason}")
    
    df = pd.read_csv(StringIO(csv_data))
    
    return df
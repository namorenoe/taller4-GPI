# Este archivo limpia los datos

import numpy as np
import pandas as pd

# Funcion para simular datos usando numpy
def simular_datos():
    np.random.seed(50)
    data = {
        'A': np.random.normal(0, 1, 100),
        'B': np.random.normal(5, 2, 100),
        'C': np.random.normal(-3, 1.5, 100)
    }
    df = pd.DataFrame(data)
    return df
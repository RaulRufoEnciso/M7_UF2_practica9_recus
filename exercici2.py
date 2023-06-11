import numpy as np

# Funcion para crear una array normal
def crear_array():
    a = np.array([88,23,39,41])
    return a;

# Funcion para crear una array de arrays
def crear_array_de_arrays():
    b = np.array([[7.64,21.7,38.4],[41.2,52.8,68.9]])
    return b;

# Funcion para crear una funcion vertical
import numpy as np

def create_vertical_array(numbers):
    # Crear un ndarray vertical utilizando la función array de NumPy
    array = np.array(numbers).reshape(-1, 1)
    return array

# Imprimimos las funciones para ver su resultado
print(crear_array())
print(crear_array_de_arrays())
print(create_vertical_array([12, 4, 9, 8]))
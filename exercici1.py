import numpy as np

def ndarray():
  # Creamos una matriz de zeros con dimensiones 50x50
  matriz = np.zeros((50,50), dtype=int)

  # Rellenamos la diagonal con numeros ascendentes de 0 a 49
  np.fill_diagonal(matriz, np.arange(50))

  # Retornamos la matrizz
  return matriz;

# Llamada a la funcion
print(ndarray())



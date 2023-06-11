import numpy as np

# Crea una matriz de dimensiones 4x3 con numeros aleatorios del 0 al 80
def crear_matriu():
    matriu = np.random.randint(0, 81, size=(4, 3))
    return matriu

# Modifica la ultima matriz para que sea de dimensiones 3x4 y que la ultima columna se convierta en la ultima fila
def modificar_matriu_1(matriu):
    matriu_modificada = np.transpose(matriu)
    return matriu_modificada

# La nueva matriz deberá tener los mismos números en la última columna
def modificar_matriu_2(matriu):
    ultima_columna = matriu[:, -1]
    matriu_modificada = np.hstack((matriu[:, :-1], ultima_columna.reshape(-1, 1)))
    return matriu_modificada

# Ejemplo de uso de las funciones
matriu_original = crear_matriu()
print("Matriu original:")
print(matriu_original)

matriu_modificada_1 = modificar_matriu_1(matriu_original)
print("Matriu modificada (1):")
print(matriu_modificada_1)

matriu_modificada_2 = modificar_matriu_2(matriu_original)
print("Matriu modificada (2):")
print(matriu_modificada_2)

import numpy as np

# Genera una matriz random de 0 al 100 con las dismensiones pasado por consola
def generar_matriu_random():
    dimensio = int(input("Introdueix la dimensió de la matriu: "))
    matriu = np.random.randint(0, 100, size=(dimensio, dimensio))
    return matriu

# Busca en la matriz el numero maximo de la matriz
def valor_maxim(matriu):
    max_value = np.max(matriu)
    return max_value

# Busca en la matriz el numero minimo de la matriz
def valor_minim(matriu):
    min_value = np.min(matriu)
    return min_value

# Ejemplo de uso de las funciones
matriu = generar_matriu_random()

# Mostrar la matriz por consola
print(matriu)

maxim = valor_maxim(matriu)
print("Valor màxim de la matriu:", maxim)

minim = valor_minim(matriu)
print("Valor mínim de la matriu:", minim)

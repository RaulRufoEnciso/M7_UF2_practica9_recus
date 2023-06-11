import exercici1 as ex1
import exercici2 as ex2
import exercici3 as ex3
import exercici4_RaulRufo as ex4

# Ejercicio 1
print("Mostra en una matriz donde solo se quieren numeros ascendentes en la diagonal de '0 a 49'")
print(ex1.ndarray())

# Ejercicio 2
print("Ejercicio 2")
print("Array nueva:")
print(ex2.crear_array())
print("Array de arrays:")
print(ex2.crear_array_de_arrays())
print("Array con reshape(4,1):")
print(ex2.create_vertical_array([12, 4, 9, 8]))

# Ejercico 3
matriu = ex3.generar_matriu_random()
# Mostrar la matriz por consola
print(matriu)

maxim = ex3.valor_maxim(matriu)
print("Valor maximo de la matriz:", maxim)

minim = ex3.valor_minim(matriu)
print("Valor minimo de la matriz:", minim)

# Ejercicio 4
# Ejemplo de uso de las funciones
matriu_original = ex4.crear_matriu()
print("Matriu original:")
print(matriu_original)

matriu_modificada_1 = ex4.modificar_matriu_1(matriu_original)
print("Matriu modificada (1):")
print(matriu_modificada_1)

matriu_modificada_2 = ex4.modificar_matriu_2(matriu_original)
print("Matriu modificada (2):")
print(matriu_modificada_2)


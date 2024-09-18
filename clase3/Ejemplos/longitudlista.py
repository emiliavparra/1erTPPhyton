# La longitd de una lista vacia
lista_vacia = []
print('Longitud de una lista vacia', len(lista_vacia))

# Lista con enteros
# La longitud es igual al numero de elementos que tiene la lista
lista_de_enteros = [1, 2, 3, 4, 5]
print('La longitud de una lista de enteros es: ', len(lista_de_enteros))

# Lista con cadenas
# La longitud es igual al numero de elementos de la lista
lista_cadenas = ['manzana', 'banana', 'cereza']
print('Longitud de una lista de cadenas es de: ', len(lista_cadenas))

# Lista mixta
# La longitud cuenta todos los elementos(sin importar el tipo de elemento)
lista_mixta = [1, 'texto', 3.14, [1, 2, 3]]
print('La longitud en la lista mixta es de: ', len(lista_mixta))

# Lista con elementos repetidos
# La longitud es el resultado de multiplicar elementos repetidos
lista_repetidos = [0] * 10
print('Longitud de una lista de repetidos: ', len(lista_repetidos))

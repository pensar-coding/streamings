from functools import reduce

lista_numeros = [0, 1, 2, 3, 4, 5]

#filter
impares = list(filter(lambda x: x % 2 != 0,lista_numeros))
print(impares)

#reduce
suma = reduce(lambda a,b: a+b, impares)
print(suma)


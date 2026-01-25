



lista = ['a','b','c','d']

for i, letra in enumerate(lista, 1):
    print(i,letra)
print('------------')

for i in range(len(lista)):
    print(i+1,lista[i])

print('------------')


lista2 = [1,2,3,4,5,6,7,8,9,10]
def n_cuadrados (lista):
    return [n**2 for n in lista]

print(n_cuadrados(lista2))

print('------------')

def n_cuadrados_pares(lista):
    return [n**2 for n in lista if n % 2 == 0]

print(n_cuadrados_pares(lista2))

print('------------')

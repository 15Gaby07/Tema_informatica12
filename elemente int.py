def creare_lista_int():
    n = int(input('Nr. de elemente = ? '))
    lista_locala = []
    for i in range(n):
        elem = int(input('Elementul ' + str(i) + ' este: '))
        lista_locala.append(elem)
    return lista_locala

lista1 = creare_lista_int()
print(lista1)
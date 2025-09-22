def creare_lista_int():
    n = int(input('Nr. de elemente = ? '))
    lista_locala = []
    for i in range(n):
        elem = float(input('Elementul ' + str(i) + ' este: '))
        lista_locala.append(elem)
    return lista_locala

lista2 = creare_lista_int()
print(lista2)
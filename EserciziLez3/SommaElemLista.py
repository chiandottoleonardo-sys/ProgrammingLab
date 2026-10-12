def SommaElemLista(lista):
    valore = 0
    for elemento in lista:
        valore += elemento
    return valore

numeri = [5, 1, 54]
risultato = SommaElemLista(numeri)
print(risultato)
        
def elemInComune(lista1, lista2):

    return len(set(lista1) & set(lista2)) > 0

a = [1,0,5,3,2]
b = [4,7,8,9,2]
c = [1,3,5,0]

print(elemInComune(a, b))
print(elemInComune(b, c))


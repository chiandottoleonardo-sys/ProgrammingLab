numero = int(input("Inserire un numero intero maggiore di 1: "))

count = 0

for test in range(2, numero):
    if(numero%test == 0):
        count += 1

if(count != 0):
    print(f"{numero} non è primo")
else:
    print(f"{numero} é primo")
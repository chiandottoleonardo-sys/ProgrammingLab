def fattoriale(numero):
    risultato = 1
    for i in range(2, numero+1):
        risultato *= i
    return risultato

numero = int(input("Inserire un intero: "))
fatNumero = fattoriale(numero)

print(fatNumero)
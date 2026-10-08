somma = 0

print("Inserisci un numero da sommare(0 per terminare): ")

numero = float(input("Inserisci un numero: "))

while numero != 0:
    somma += numero

    numero = float(input("Inserisci un altro numero(0 per fermarti):"))

print(f"La somma totale è {somma}")


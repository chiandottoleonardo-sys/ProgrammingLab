def dizionario(lista):
    conteggio = {}
    for parola in lista:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1
    return conteggio


parole = ["mario", "maria", "luca", "stefano", "maria"]
print(f"Dizionario:",dizionario(parole))
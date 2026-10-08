def ContaLettera(lettera, parola):
    count = 0
    for carattere in parola:
        if(carattere == lettera):
            count += 1
    return count

Parola = str(input("Inserire una parola: "))
Lettera = str(input("Inserire una lettera: "))
risultato = ContaLettera(Lettera, Parola)
print(risultato)
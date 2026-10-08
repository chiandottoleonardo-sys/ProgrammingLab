def conta_vocali(testo):

    vocali = "aeiouAEIOUàèìòù"

    count = 0

    for carattere in testo:
        if carattere in vocali:
            count += 1

    return count

testo = str(input("Inserire una frase: "))

risultato  = conta_vocali(testo)

print(f"In '{testo}' ci sono {risultato} vocali. ")
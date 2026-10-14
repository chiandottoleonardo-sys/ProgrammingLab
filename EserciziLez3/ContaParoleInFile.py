def conta_parole(file, parola_cercata):
    count = 0

    with open(file, 'r') as F:

        for linea in F:
            parole = linea.split()

            for p in parole:
                if p == parola_cercata:
                    count += 1

    return count

tot = conta_parole('testo.txt', 'mare')
print(tot)
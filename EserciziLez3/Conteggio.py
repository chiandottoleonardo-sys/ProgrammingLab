def conteggio(file):
    dict = {}
    with open(file, 'r') as f:
        for linea in f:

            linea_pulita = (linea
                            .replace(',', ' ')
                            .replace('.', ' ')
                            .replace(';', ' ')
                            .replace(':', ' ')
                            .replace('!', ' ')
                            .replace('?', ' '))

            parole = linea_pulita.split()

            for p in parole:

                if p in dict:
                    dict[p] += 1
                else:
                    dict[p] = 1
    return dict

dizionario = conteggio('testo.txt')
print(dizionario)

        
            
def somma_vendite(file):
    with open(file, 'r') as my_csv:
        somma = 0.0
        next(my_csv)

        for column in my_csv:
            valori = column.split(',')

            if valori[0] != 'Sales':
                sales = valori[0]
                value = valori[1]
                somma = somma + float(value)

        return(somma)
    
print(somma_vendite('shampoo.csv'))
    
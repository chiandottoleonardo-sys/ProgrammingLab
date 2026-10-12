def numeri_in_parole_manuale(lista_numeri):
    mappa = ["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
    
    lista_risultato = []
    
    for num in lista_numeri:
        parola = mappa[num]       
        lista_risultato.append(parola)
        
    return lista_risultato


x = [1,2,5,6]
print(numeri_in_parole_manuale(x)) 
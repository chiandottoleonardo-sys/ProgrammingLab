class CSVFile():

    def __init__(self, name):

        self.name = name

    def get_data(self):
        dati = []

        with open(self.name, 'r') as file:
            for riga in file:

                elementi = riga.strip().split(',')
                dati.append(elementi)

        return dati

file = CSVFile("shampoo.csv")
contenuto = file.get_data()
print(contenuto)
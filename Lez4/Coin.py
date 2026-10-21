import random

class Coin():

    def __init__(self):

        self.faccia = None

    def __str__(self):
            return 'Coin "{}"'.format(self.faccia)

    def lancia(self):

        risultati = ["Testa", "Croce"]
        self.faccia = random.choice(risultati)

    def get_face(self):
        return self.faccia

moneta = Coin()

moneta.lancia()

print("Il lancio della moneta ha dato:", moneta.get_face())

    
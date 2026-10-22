class Veicolo():

    def __init__(self, modello, marca, anno):

        self.marca = marca
        self.modello = modello        
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return 'Veicolo = {} {} {} {}km/h'.format(self.marca, self.modello, self.anno, self.speed)

    def accellerare(self):
        self.speed += 5

    def frenare(self):
        if(self.speed >= 5):
            self.speed -= 5
        else: 
            self.speed = 0

    def get_speed(self):
        return self.speed

class Auto(Veicolo):

    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
        self.speed = 0

    def __str__(self):
        return 'Veicolo = {} {} {} - porte {} - {}km/h'.format(self.marca, self.modello, self.anno, self.numero_porte, self.speed)

class Moto(Veicolo):
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo
        self.speed = 0

    def __str__(self):
        return 'Veicolo = Moto {} {} {} - tipo: {} - {}km/h'.format(self.marca, self.modello, self.anno, self.tipo, self.speed)
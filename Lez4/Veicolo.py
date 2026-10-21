class Veicolo():

    def __init__(self, modello, marca, anno, targa):

        self.marca = marca
        self.modello = modello        
        self.anno = anno
        self.targa = targa
        self.speed = 0

    def __str__(self):
        return 'Veicolo = {} {} {} {} {}km/h'.format(self.marca, self.modello, self.anno, self.targa, self.speed)

    def accellerare(self):
        self.speed += 5

    def frenare(self):
        if(self.speed >= 5):
            self.speed -= 5
        else: 
            self.speed = 0

    def get_speed(self):
        return self.speed

auto = Veicolo("Volkswagen", "Golf", 2021, "GD129PF")

print(auto)

auto.accellerare()
auto.accellerare()
print("Velocità:", auto.get_speed())

auto.frenare()
print("Velocità:", auto.get_speed())

print(auto)
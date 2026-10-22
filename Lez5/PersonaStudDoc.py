class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi  

    def saluta(self):
        Persona.saluta(self)
        print("Frequento i corsi:")
        for corso in self.corsi:
            print(f"  - {corso}")
        

class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi  
  
    def saluta(self):
        Persona.saluta(self)  
        print("Frequento i corsi:")
        for corso in self.corsi:
            print(f"  - {corso}")


Studente1 = Studente("Leonardo", "Chiandotto", ["Analisi 1", "Algebra Lineare", "Programmazione in C"])
Studente1.saluta()

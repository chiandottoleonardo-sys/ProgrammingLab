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

    def insegna_tutti_corsi(self, studente):
        return set(studente.corsi).issubset(set(self.corsi))


def verifica_presenza_docenti_corsi(lista_studenti, lista_docenti):
    for studente in lista_studenti:
        studente_coperto = False

        for docente in lista_docenti:
            if docente.insegna_tutti_corsi(studente):
                studente_coperto = True
                break

        else:
            return False

    return True

Studente1 = Studente("Leonardo", "Chiandotto", ["Analisi 1", "Algebra Lineare", "Programmazione in C"])
Studente1.saluta()

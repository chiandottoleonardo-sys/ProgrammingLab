import random

class Person():
#funzione x inizializzare una classe
    def __init__(self, name, surname):

        self.name    = name
        self.surname = surname
#
    def __str__(self):
        return 'Person "{} {}"'.format(self.name, self.surname)
#
    def say_hi(self):

        random_number = random.randint(0,2) 

        if random_number == 0:
            print('Hello, i am {} {}.'.format(self.name, self.surname))
        elif random_number == 1:
            print('Hi, i am {} {}!'.format(self.name, self.surname))
        elif random_number == 2:
            print('Yo bro! {} here!'.format(self.name))  

person = Person('Leonardo', 'Chiandotto')
print(person)
person.say_hi()

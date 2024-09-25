#!/bin/python
# ctrl shift 7
import os

os.system ("clear")

# class person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#         print ("person opprettet")

#     def greet(self):
#         print (f"Jeg heter {self.name}, og er {self.age} år gammel")

# person1 = person("Bob",31)
# print (person1.name)
#person1.greet()

# class Konto: 
#     def __init__(self, saldo, navn):
#         self.__saldo = saldo
#         self.__navn = navn
    
#     def innskudd(self, inn):
#         self.__saldo += inn
    
#     def uttak(self, ut):
#         if ut <= self.__saldo:
#             self.__saldo -= ut
#         else:
#             print("ikke nok penger")

#     def get_saldo(self):
#         return self.__saldo
    
#     def get_navn(self):
#         return self.__navn
    
#     def set_navn(self, nytt):
#         self.__navn = str(nytt)
        
# min_konto = Konto(150,"bruks")
# print(min_konto.get_saldo())
# min_konto.uttak(200)
# min_konto.innskudd(50)
# print (min_konto.get_saldo())
# min_konto.set_navn("Spare")
# print(min_konto.get_navn())

class Dyr:
    def __init__(self, navn):
        self.navn = navn

    def make_sound(self, sound):
        self.sound = sound
        print (f"{self.navn} sier {self.sound}")

class Hund(Dyr):
    def make_sound(self):
        super().make_sound("wof wof")
    def logre(self):
        print(f"{self.navn} logrer")
        
class Katt(Dyr):
    def make_sound(self,):
        super().make_sound("meow")
  
       


hund1 = Hund("Fido")
hund1.make_sound() 
hund1.logre()

katt1 = Katt("katt")
katt1.make_sound()
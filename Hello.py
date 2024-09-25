#!/bin/python
from typing import no_type_check
import os 

navn = "bib"
cal = input()
#output = steam.read()

os.system("clear")
#print ("Hello bob!")
#print ("Hei, " + navn)
print ("Hello " + cal)
#os.system (output)

def goblin(navn = "glor", alder = 75):
    print (f"Bra ser du ikke {navn} {alder}")

bruker = "bob", 84

goblin ()
goblin(bruker)
goblin("we", 23)
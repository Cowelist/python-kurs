#!/usr/bin/python
import os
import re

os.system("clear")

def matte():
    try:
        usr_input1 = int(input("Skriv et tall du skal dele \n" ))
        usr_input2 = int(input("Skriv tallet du vil dele med \n"))

        resultat = usr_input1 / usr_input2
        print (f"Resultatet er {resultat}")
    except ZeroDivisionError:
        os.system("clear")
        print("Du kan ikke dele på null")
        print("prøv igjen")
        matte()
    except ValueError:
        os.system("clear")
        print("Dette er ikke et gyldig tall")
        print("prøv igjen")
        matte()  

#matte()

def fil_leser():
    folder_check()
    try: 
        fil_leser_input = str(input("Skriv ned en vil du vil lese \n"))
        path = ("uke_2/Feilaantering/" + fil_leser_input)
        f = open(path, "r")
        print(f.read())
    except FileNotFoundError:
        os.system("clear")
        print("Filen eksisterer ikke \nprøv igjen")
        fil_leser()
    except ValueError:
        print ("")
        

def folder_check():
    folder_path = ("/home/elev/Documents/GitHub/python-kurs/uke_2/Feilaantering")
    for file in os.listdir(folder_path):
        #print (file)
        if isinstance(file.isdigit, str and int):
            print (f"There are both nummbers and words in {file}")
        elif file.isdigit():
            print (f"there are only nummbers in {file}")
        elif isinstance(file, str):
            print (f"there are only words in {file}")
        else:
            pass
folder_check()
# elif isinstance(file.isdigit, int):

#fil_leser()


# var = input("Hei skriv et tall")
# var_2 = ("Hei på " + var)


# print(var_2)


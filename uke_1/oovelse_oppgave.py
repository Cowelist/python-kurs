#!/bin/python
import os 
import random

os.system ("clear")
# temperatur = int(input("Hva er temperaturen hos deg\n"))

# print (temperatur)

# if temperatur == 15: 
#     print ("Midels")
# elif temperatur < 15:
#     print ("det var kaldt")
# else:
#     print ("veldig varmt")
    



# def nummber(g):
#     num = [ g for g in range (g)if g % 2 == 0]
#     print (num)
        

# nummber (10)    

t1_ran = 1
t2_ran = 100
num = random.randint (t1_ran, t2_ran)
typing = (input(f"pick a nummber between {t1_ran} - {t2_ran} \n"))

if typing != int:
    print ("Type a nummber")
elif num == typing:
    print ("")
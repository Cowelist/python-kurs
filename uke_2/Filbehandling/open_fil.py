#!/usr/bin/python
#import read
import os

#os.system ("clear")

read_file = "uke_2/Filbehandling/read.txt"

#def open(r):
    # for r in lese_fil:
    #     print ()
# with open(read_file, "r") as f:
#     #os.system("clear")
#     print(f.read())
#     f.close()
# f = open(read_file, "r")
# print (f.read())

# with open(read_file, "w") as f:
#     command = input()
#     f.write(command)

# with open(read_file, "a") as f:
#     usr_input = input("\n")
#     f.write(usr_input + "\n")




typo = "r"
usr_input_2 = input("\n")
f = open(read_file, typo)

def write():
    typo = "w"  
    f.write(usr_input_2 + "\n")
    f.close()
    print ("w")

def a_write():
    typo = "a"
    f.write(usr_input_2 + "\n")
    f.close()
    print ("a")
    


if os.stat(read_file).st_size == 0:
    
    write()
    
else: 
    
    a_write()



print (os.stat(read_file).st_size)
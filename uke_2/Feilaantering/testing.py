#!/usr/bin/python
import os 
import re

files = []

os.system ("clear")
path = ("/home/elev/Documents/GitHub/python-kurs/uke_2/Feilaantering")
for file in os.listdir(path):
    files.append(file)


var = ("w2.py")

def finner_int_str():
    for a in files:
        if re.search(r'\d', a):
            print("int here")
        else:
            print("no int") 



def re_dot():
    Con = ("")  

    patern =re.compile(r'[^a-zA-Å0-9._-]')

    check = set(Con)

    after_dot = Con.split('.', 1)[0]

    match = patern.findall(after_dot)

    check.update(match)

    if check:
        print ("before")
    else:
        print ("after")

def os_dot():    
    for a in os.listdir(path):
        if not a.startswith("."):
            remove = a.split(".")[0]
            files.append(remove)
            print (remove)

    for a in files:
        if re.search(r'\d', a):
            print("int here")
        else:
            print("no int") 



os_dot()

# for a in files:
#     if re.search(r'\d', a):
#         print("int here")
#     else:
#         print("no int") 














def folder_check():
    folder_path = ("/home/elev/Documents/GitHub/python-kurs/uke_2/Feilaantering")
    for file in os.listdir(folder_path):
        #print (file)
        for a in files:
            if isinstance(a, str and int):
                print (f"There are both nummbers and words in {file}")
            elif isinstance(a, int):
                print (f"there are only nummbers in {file}")
            elif isinstance(a, str):
                print (f"there are only words in {file}")
            else:
                pass
#folder_check()
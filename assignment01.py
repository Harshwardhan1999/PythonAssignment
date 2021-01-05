#question1
#Write a Python program to read a file line by line and store it into a list.


File_List=[]
def read_file(file_name):
    with open(file_name) as file:
        for l in file:
            File_List.append(l.strip())     #strip() method return copy of string.

read_file('C:\seleniumProject/assig1.txt')
#question5
#Write a Python program that takes a text file as input and returns the number of
#words of a given text file.

def count_file_words(file_path):

   with open(file_path) as file:

       data = file.read()
       data.replace(",", " ")    #replace space with comma
       return len(data.split(" "))

count_file_words('C:\seleniumProject/assign05.txt')
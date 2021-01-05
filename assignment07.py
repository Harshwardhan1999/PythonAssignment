#question7
# Write a script which can read the files line by line with .log ext and print it into a
#file , while printing the data from the suffix with present date and time of the system.

import logging

def add_current_datetime (myfile):
    #myfile  is the file which we want to read
    logging.basicConfig(level=logging.DEBUG, filename='C:\seleniumProject/log2.txt', format='%(asctime)s %(levelname)s:%(message)s')
    #filename is file where we have to print it into file
    try:
        with open(myfile, 'r') as f:
            file_data = f.read()
            logging.debug(file_data)

    except OSError as e:
        logging.error("error reading the file")

add_current_datetime('C:\seleniumProject/log1.txt')
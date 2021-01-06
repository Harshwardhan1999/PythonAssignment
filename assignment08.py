#question8
# Program to Generate random logs and write in a file , once the file size reaches 2Mb
#open new file and continue writing


import os

def convert_bytes(file_size):

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if file_size < 1024.0:
            return "%3.1f %s" % (file_size, x)
        file_size /= 1024.0


def find_file_size(file):

    if os.path.isfile(file):
        file_info = os.stat(file)
        return convert_bytes(file_info.st_size)


file_path = "C:\seleniumProject/log1.txt"
file_path1 = "C:\seleniumProject/log2.txt"

size1=find_file_size(file_path)
while( str(size1)=="2 MB"):
    with open(file_path, "w") as fh:
        fh.writelines('#file , while printing the data from the suffix with present date and time of the system.')

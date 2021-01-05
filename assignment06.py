#question6
#Write a Python program to convert an array to an array of machine values and
#return the bytes representation.

import array
import binascii

def convert_array(array_name):
    print("Original array:")
    print('A1:', array_name)
    bytes_array = array_name.tobytes()
    print('Array of bytes:', binascii.hexlify(bytes_array))

array1 = array.array('i',[1,2,3,4,5,6])
convert_array(array1)

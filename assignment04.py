#question4
#Write a Python program to sort a list of dictionaries using Lambda.
dictionary_list= [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2','color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_dictionary_list = sorted(dictionary_list, key = lambda x: x['color'])
print("\nSorted list of dictionaries:")
print(sorted_dictionary_list)
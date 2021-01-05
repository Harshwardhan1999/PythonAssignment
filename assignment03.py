#question3
#Write a Python program to convert the Python dictionary object (sort by key) to
#JSON data. Print the object members with indent level 4.

import json
dictionary1 = {8: 'harsh', 88: 'kumar', 12: 'thakur', 90: 'mumbai'}

print("\nJSON data:")
print(json.dumps(dictionary1, sort_keys=True, indent=4))
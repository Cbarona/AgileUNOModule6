"""
Carlos Barona
Module 6
"""

import sys
import json


with open("input.json", "r") as inport:
    customers = json.load(inport)

# Are all customer numbers unique?
temp = []
for value in customers["clients"]:
    temp.append(value["id"])

# Add values to set
unique = set(temp)

if len(unique) != len(temp):
    print("There are duplicate id numbers in the data, exiting!!!")
    sys.exit()
else:
    print("All customer ids are unique!!!")

"""
1.
So we know how to compare the customers to ensure their id's are unique.
Now create a set of each customer email and test for uniqueness.
Insert code below.
"""
temp = []
for value in customers["clients"]:
    temp.append(value["email"])

# Add values to set
unique = set(temp)

if len(unique) != len(temp):
    print("There are duplicate email numbers in the data, exiting!!!")
    sys.exit()
else:
    print("All customer emails are unique!!!")


"""
2.
Create a dictionary of each customer, each one should contain
the name and email of each customer.
Write this as JSON to a new file called email_list.json.
"""
def write_jsonfile(data):
    with open(input("Please name JSON file (Include \".json\" extention): "), 'w') as f:
        json.dump(data, f, indent=4)

tempdict = {}
for client in customers["clients"]:
    tempdict[client['name']] = client["email"]
write_jsonfile(tempdict)

"""
3.
Open the original file again, this time
set each male customer's
isActive status to false. Write 
this data to a file called current_customers.json.
"""
for client in customers["clients"]:
    if client['gender'] == 'male':
        client.update({"isActive":False})
write_jsonfile(customers)
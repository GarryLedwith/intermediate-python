# Dictionary is a collection of key-value pairs, unordered, mutable
# It is defined using curly braces {}.
# Each key is unique and is used to access its corresponding value.
mydict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(mydict1)

value = mydict1['name']  # Accessing value by key
print(value)  # Output: Alice

mydict2 = dict()  # Creating an empty dictionary
print(mydict2)

mydict1['email'] = 'garry@gmail.com'  # Adding a new key-value pair
print(mydict1)

# deleting items from a dictionary
del mydict1['age'] # Deleting a key-value pair by key
print(mydict1)

mydict1.pop('city')  # Removing a key-value pair and returning its value
print(mydict1)

# conditionals in dictionaries
if 'name' in mydict1:  # Checking if a key exists
    print("Name is in mydict1")
else:
    print("Name is not in mydict1")

# try except for key access
try:
    value = mydict1['age']  # Trying to access a key that may not exist
except KeyError:
    print("Key 'age' does not exist in mydict1")    
    
# Looping through a dictionary
print("Looping through mydict1:")
for key in mydict1:  # Looping through keys
    print(f"{key}: {mydict1[key]}")  # Accessing value by key
    
# Looping through with keys method
print("Looping through keys:")
for key in mydict1.keys():
    print(key)  # Printing keys
    
# Looping through with values method
print("Looping through values:")
for value in mydict1.values():
    print(value)  # Printing values
    
# Looping through with key and value pairs
print("Looping through key-value pairs:")
for key, value in mydict1.items():
    print(f"{key}: {value}")  # Printing key-value pairs
    
# copying a dictionary
mydict3 = mydict1.copy()  # Creating a shallow copy of the dictionary (pass by value)
print(mydict1)  # Original dictionary remains unchanged
print(mydict3)

# modifying the copy
mydict3['name'] = 'Bob'  # Changing the value of 'name'
print(mydict3)  # Output: {'name': 'Bob', 'email':
print(mydict1)  # Original dictionary remains unchanged

mydict4 = mydict1  # Creating a reference to the original dictionary (pass by reference)
mydict4['name'] = 'Charlie'  # Modifying the reference will change the original dictionary
print(mydict1)  # Output: {'name': 'Charlie', 'email': '

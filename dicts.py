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
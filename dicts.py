# Dictionayy is a collection of key-value pairs, unordered, mutable
# It is defined using curly braces {}.
# Each key is unique and is used to access its corresponding value.
mydict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(mydict1)

value = mydict1['name']  # Accessing value by key
print(value)  # Output: Alice

mydict2 = dict()  # Creating an empty dictionary
print(mydict2)
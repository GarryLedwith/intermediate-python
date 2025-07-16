# Tuple is a collection datatype that is ordered and immutable.
# It can hold a collection of items, which can be of different data types.
# Tuples are defined using parentheses () instead of square brackets [] like lists.
# Tuples are often used to group related data together.
# Example of a tuple containing strings
mytuple1 = ('banana', 'apple', 'orange')
print(mytuple1[0])  # Accessing the first element ('banana')
print(type(mytuple1))  # Output: <class 'tuple'>

mytuple2 = ("Hello") # This is not a tuple, it's just a string
print(type(mytuple2))  # Output: <class 'str'> (a comma is needed to create a tuple with one item)
mytuple3 = ("Hello",)  # This is a tuple with one item
print(type(mytuple3))  # Output: <class 'tuple'>

# built in tuple function
mytuple3 = tuple([1, 2, 3])  # Convert a list to a tuple
print(mytuple3)  # Output: (1, 2, 3)

# iterating through a tuple
print("Looping through mytuple1:")
for i in mytuple1:
    print(i)
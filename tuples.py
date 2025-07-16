import sys # Importing sys module for system-specific parameters and 
import timeit # Importing timeit module for measuring execution time
# Tuples in Python
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
    
    
mylist = [0, 1, 2, "three", "four"]
mytuple3 = (0, 1, 2, "three", "four")  # A tuple with mixed data types
print(sys.getsizeof(mylist))  # Get the size of the list in bytes (lists are larger than tuples)
print(sys.getsizeof(mytuple3))  # Get the size of the tuple in bytes

# Time comparison between list and tuple
print(timeit.timeit(stmt="mylist = [0, 1, 2, 'three', 'four']", number=1000000))  # Time to create a list
print(timeit.timeit(stmt="mytuple3 = (0, 1, 2, 'three', 'four')", number=1000000))  # Time to create a tuple
# Tubples are generally faster to create and access than lists due to their immutability.
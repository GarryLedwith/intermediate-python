# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() constructor.
# single element sets require a trailing comma.
# Sets are useful for membership testing and eliminating duplicate entries.

myset1 = {'banana', 'apple', 'orange'}
print(myset1)

myset2 = set()  # Creating an empty set
print(myset2)

myset3 = {}  # This is not a set, it's an empty dictionary
print(type(myset3))  # Output: <class 'dict'>

myset4 = {5, True, 'hello'}  # A set with mixed data types
print(myset4)

myset5 = {'banana', 'apple', 'orange', 'banana'}  # Duplicates are ignored
print(myset5)  # Output: {'banana', 'apple', 'orange'}
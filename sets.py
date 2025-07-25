# Sets are unordered collections of unique elements, and are mutable.
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

# Removing an item from a set
myset5.remove('apple')  # Remove an item by value (raises KeyError if not found)
print(myset5)  # Output: {'banana', 'orange'}

# disgarding an item from a set
myset5.discard('banana')  # Discard an item by value (does not raise an error if not found)
print(myset5)  # Output: {'orange'}

# clear a set
myset5.clear()  # Remove all items from the set
print(myset5)  # Output: set()

# iterating through a set
myset6 = {'banana', 'apple', 'orange'}
print("Looping through myset6:")
for i in myset6:
    print(i)
    
# conditionals in sets
if 'banana' in myset6:
    print("Banana is in myset6")
else:
    print("Banana is not in myset6")    
    
# Union and Intersection of sets
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union of sets (union combines all unique elements from both sets without duplicates)
u = odds.union(evens)  # or odds | evens
print("Union of odds and evens:", u)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection of sets (intersection returns only the elements that are present in both sets)
i = odds.intersection(evens)  # or odds & evens
print("Intersection of odds and evens:", i)  # Output: set() (no common elements)

# Intersection with primes
i_primes = odds.intersection(primes)
print("Intersection of odds and primes:", i_primes)  # Output: {3, 5, 7}

# calculating the difference between sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
difference = setA.difference(setB)  # or setA - setB
print("Difference between setA and setB:", difference)  # Output: {1, 2, 3}

dirrerence2 = setB.difference(setA)  # or setB - setA
print("Difference between setB and setA:", dirrerence2)  # Output: {10, 11, 12}

# symmetric difference (elements that are in either set but not in both)
symmetric_diff = setA.symmetric_difference(setB)  # or setA ^ setB
print("Symmetric difference between setA and setB:", symmetric_diff)  # Output: {4, 5, 6, 7, 8, 9, 10, 11, 12}

setA.update(setB)  # Update setA with elements from setB (union)
print("Updated setA after union with setB:", setA)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}   

# intersection update (keep only elements that are in both sets)
setA.intersection_update(setB)  # Keep only elements that are in both sets
print("setA after intersection update with setB:", setA)  # Output: {1, 2, 3}
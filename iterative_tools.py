# Iterative tools: This module provides tools for iterating over collections in Python.
# It includes functions for filtering, mapping, and reducing collections.
# product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product  # Cartesian product of input iterables
from itertools import permutations  # All possible orderings of input iterable
from itertools import combinations  # All possible combinations of input iterable
from itertools import accumulate  # Accumulate results of a binary function
from itertools import groupby  # Group consecutive elements in an iterable
from itertools import count, cycle, repeat  # Infinite iterators for counting, cycling through elements
# Example of using product
a = [1, 2]
b = [3, 4]
prod = product(a, b)  # Cartesian product of a and b
print(list(prod))  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

# Example of using permutations 
perm = permutations(a)  # All possible orderings of a
print(list(perm))  # Output: [(1, 2), (2, 1)]

# Example of using combinations
comb = combinations(a, 2)  # All possible combinations of a taken 2 at a time
print(list(comb))  # Output: [(1, 2)]

# Example of using accumulate
from operator import add  # Importing add function for accumulation
acc = accumulate(a, add)  # Accumulate the sum of elements in a
print(list(acc))  # Output: [1, 3] (1 + 2)

# Multiplying elements using accumulate
import operator  # Importing operator module for other functions
a = [1, 2, 3, 4]
acc2 = accumulate(a)  # Default is to accumulate using addition
print(list(acc2))  # Output: [1, 3, 6, 10]
acc2 = accumulate(a, func=operator.mul)  # Default is to accumulate using addition

# Example of using groupby
# returns keys and groups of consecutive elements
def smaller_than_3(x):
    return x < 3

a = [1, 2, 2, 3, 4, 1, 2, 3]

group_obj = groupby(a, key=smaller_than_3)  # Group elements based on the condition
for key, group in group_obj:
    print(key, list(group))  # Output: True [1, 2, 2], False [3, 4], True [1, 2], False [3]




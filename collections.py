# Collectiosn module 
# Collections are specialized container datatypes in Python that provide alternatives to built-in types 
# like lists, tuples, and dictionaries.
# Collections: Counter, namedtuple, deque, defaultdict, OrderedDict
# Counter
from collections import Counter # Counter is a subclass of dict that counts hashable objects.
from collections import namedtuple # namedtuple is a factory function for creating tuple subclasses with named fields.
from collections import deque # deque is a double-ended queue that supports adding and removing elements from both ends.
from collections import defaultdict # defaultdict is a subclass of dict that returns a default value for missing keys.
from collections import OrderedDict # OrderedDict is a subclass of dict that maintains the order of insertion of keys.
# Example of using Counter
a = "aaaaabbbb"
my_counter = Counter(a)  # Count the frequency of each character in the string
print(my_counter)  # Output: Counter({'a': 5, 'b': 4})
print(my_counter['a'])  # Accessing the count of 'a' (Output: 5)
print(my_counter.most_common(2))  # Get the two most common elements (Output: [('a', 5), ('b', 4)])

# Example of using namedtuple
Point = namedtuple('Point', ['x', 'y'])  # Create a named tuple
p = Point(10, 20)  # Create an instance of the named tuple
print(p)  # Output: Point(x=10, y=20)
print(p.x, p.y)  # Accessing fields by name (Output: 10 20)

     
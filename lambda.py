# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
# Lambda syntax: lambda arguments: expression
# typically used in higher-order functions like map, filter, and reduce.
# Example of a simple lambda function
add = lambda x, y: x + y  # A lambda function that adds two numbers
print(add(2, 3))  # Output: 5

add10 = lambda x: x + 10  # A lambda function that adds 10 to its argument
print(add10(5))  # Output: 15

# sorted lists example using lambda
points2D = [(1, 2), (3, 1), (5, 0), (2, 4)]
# Sort points by the second element of the tuple
sorted_points = sorted(points2D, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, 0), (3, 1), (1, 2), (2, 4)]
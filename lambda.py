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
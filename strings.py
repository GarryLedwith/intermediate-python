# strings are immutable
my_string = 'single line string'  # Single line string
char = my_string[0]  # Accessing the first character
print(char)  # Output: s
substring = my_string[0:5]  # Slicing the string from index 0 to 4
substring2 = my_string[::2]  # Slicing the string with a step of 2
substring3 = my_string[:-1]  # Reversing the string
print(substring)  # Output: singl
print(substring2)  # Output: sgleine trng
print(substring3)  # Output: single line string

# LIsts in Python
mylist1 = ['banana', 'apple', 'orange']

print(mylist1)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, 'hello']
print(mylist3)

item = mylist1[0-1]
print(item)

# loop through a list (for loop)
print("Looping through mylist1:")
for i in mylist1:
    print(i)
    
# conditionals 
if 'banana' in mylist1:
    print("Banana is in mylist1")
else:
    print("Banana is not in mylist1")
  
# List methods    
print(len(mylist1))  # Get the length of the list
mylist1.append('kiwi')  # Add an item to the end of the list
print(mylist1)
mylist1.insert(1, 'grape')  # Insert an item at a specific position
print(mylist1)
mylist1.remove('apple')  # Remove an item by value
print(mylist1)
mylist1.pop()  # Remove the last item and return it
print(mylist1)

mylist4 = [1, 3, 6, 2, 5]
print(mylist4)
# Sort the list
#mylist4.sort()  # Sort the list in ascending order (mutates the list!!)
print(mylist4)

newlist = sorted(mylist4)  # Sort the list and return a new sorted list
print(newlist)
print(mylist4)  # Original list remains unchanged

mylist5 = [0] * 10  # Create a list with 10 zeros
print(mylist5)

mylist4 + mylist5  # Concatenate two lists
print(mylist4 + mylist5)

# Slicing a list (using the colon operator)
print(mylist4[1:3])  # Get a slice of the list from index 1 to 2
print(mylist4[:3])   # Get a slice from the start to index 2
print(mylist4[2:])   # Get a slice from index 2 to the end
print(mylist4[-1])   # Get the last item
print(mylist4[-3:])  # Get the last three items
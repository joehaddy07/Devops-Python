# A tuple in Python is a collection which is ordered and immutable 
# (meaning it cannot be changed). Tuples are written with round brackets () 
# and can contain elements of different data types

# Create a Tuple:

# Empty Tuple: You can create an empty tuple by using empty parentheses.
details= ()

# Single-element Tuple: For a single element, you need a comma after the element to make it a tuple.
details= (2,)

# Nested Tuples:Tuples can contain other tuples, forming a nested structure.
nested_tuple = ((1, 2, 3), ("apple", "banana"), (True, False))
print(nested_tuple)
# Output: ((1, 2, 3), ('apple', 'banana'), (True, False))

# Accessing elements inside a nested tuple
print(nested_tuple[1][0])  # Output: apple

# Tuple Packing and Unpacking
# (1)Packing refers to assigning values to a tuple.
# (2)Unpacking allows you to assign tuple values to individual variables.
# Packing
packed_tuple = ("John", 25, "Developer")

# Unpacking
name, age, profession = packed_tuple
print(name)       # Output: John
print(age)        # Output: 25
print(profession) # Output: Developer


# Concatenating and Repeating Tuples: You can concatenate two or more tuples and repeat them using the + and * operators.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
concat_tuple = tuple1 + tuple2
print(concat_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeat_tuple = tuple1 * 3
print(repeat_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)





# Basic Tuple:A tuple can store different types of elements, such as integers, strings, and floats.
details = ("apple",2, "banana", 'cherry', "apple", "cherry",4.5)
print(details)

# access the first elements from a tuple
print(details [0])

# access the last elements from a tuple
print(details [-1])

# access elements in tuple using slicing.access 2 and banana
print(details [1:3])

# #the length of items in the tuple:
print(len(details))

# add elements in tuple 
new_detail= details + ("watermalon",)
print(new_detail)

# We can loop through a tuple using a for loop
for detail in details:
    print(details)

#using while loop to loop through a tuple
details = ("apple",2, "banana", 'cherry', "apple", "cherry",4.5)
while True:
 if "apple" in details:
  print("yes it belong there")
  break
 else:
  print("no it does not belong there")

    # check if an item exist
details= ("apple",2, "banana", 'cherry', "apple", "cherry",4.5)
print("apple" not in details)

# check if an item exist
details= ("apple",2, "banana", 'cherry', "apple", "cherry",4.5)
print("apple" in details)

 

# Tuples allow duplicate values: check how many time an item appears in the tuple
details = ("apple",2, "banana", 'cherry', "apple", "cherry",4.5)
detail= details.count("cherry")
print(detail)

details = ("apple", 2, "banana", 'cherry', "apple", "cherry", 4.5)
print(details.count("apple"))

# Index of an Element: You can find the index of the first occurrence of an element
print(details.index("cherry"))  # Output: 3




# How to remove item from tuple
details = ("apple", 2, "banana", "cherry", "apple", "cherry", 4.5)

# Convert the tuple to a list
details_list = list(details)

# Remove the first occurrence of the element "cherry"
details_list.remove("cherry")

# Convert the list back to a tuple
new_details = tuple(details_list)

print(new_details)












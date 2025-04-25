#Certainly! In Python, a for loop is used to iterate over a sequence 
#(such as a list, tuple, string, or range) or other iterable objects. Here are some examples:

#Iterating over a list:
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

#Iterating over a string:
message = "Hello, Python!"
for char in message:
    print(char)

#Iterating over a range of numbers:
for num in range(1, 5):
    print(num)

#Iterating over a tuple:
coordinates = (3, 5)
for coordinate in coordinates:
    print(coordinate)

#Iterating over a Dictionary (keys)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

#Iterating over a Dictionary (key-value pairs)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)


 


#Using enumerate to get both index and value:
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

#Nested loops (loop within a loop):
for i in range(3):
    for j in range(2):
        print(f'({i}, {j})')

#Looping with break and continue:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    if num == 7:
        break     # Stop when reaching 7

    # Define a tuple named 'fruits' containing three elements: an integer 3, a string "banana", and a string 'orange'.
fruits = (3, "banana", 'orange')

# Iterate over each element in the 'fruits' tuple.
for fruit in fruits:
    # Check if the current 'fruit' is equal to the integer 3.
    if fruit == 3:
        # If the current 'fruit' is 3, print a message indicating that the number is found.
        print(f"Found the number: {fruit}")
        # Exit the loop using the 'break' statement.
        break
    else:
        # If the current 'fruit' is not 3, print a message indicating that it belongs in the fruit category.
        print(f"does not belong in fruit: {fruit}")

# End of the loop.

    
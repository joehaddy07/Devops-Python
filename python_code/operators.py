#Assignment: Operation used to assign values to variable.

#Compareison: Comperation values and return if the comparison is true or false.

#Membership: Can be used to test whether a value is a member of a sequence, like strings, lists, or tuples.

#Arithmetic: Can be used to concatenate strings.

#Logical: Can be used to combine conditional statements.

def main():
    """Assignment: Operation"""

#Python arithmetic operators are used to perform mathematical operations like 
# addition, subtraction, multiplication, division, modulus, exponentiation, 
# and floor division on numeric values.

# Python arithmetic operators example
a = 7
b = 2

# addition
print('Sum: ', a + b) # Sum: 9

# subtraction
print('Difference: ', a - b) # Difference: 5

# multiplication
print('Product: ', a * b) # Product: 14

# division
print('Quotient: ', a / b) # Quotient: 3.5

# modulus
print('Remainder: ', a % b) # Remainder: 1

# exponentiation
print('Power: ', a ** b) # Power: 49

# floor division
print('Floor quotient: ', a // b) # Floor quotient: 3




#Membership operators: These operators are used to check if a value or a variable is present in a sequence, 
# such as a list, a tuple, a string, or a dictionary. For example::.

# Create a list of fruits.
fruits = ["apple", "banana", "cherry"]

# Use the 'in' operator to check if a value is in the list.
print("apple" in fruits) # prints True (apple is in the list)
print("orange" in fruits) # prints False (orange is not in the list)

# Use the 'not in' operator to check if a value is not in the list.
print("apple" not in fruits) # prints False (apple is in the list)
print("orange" not in fruits) # prints True (orange is not in the list)



#Compareison: comparison operators are used to compare two values and return a boolean value (True or False) as the result.

     # Define some variables
x = 10
y = 20
z = 30

# Check if x is greater than y
print(x > y) # Output: False

# Check if y is equal to z
print(y == z) # Output: False

# Check if x is less than y and y is less than z
print(x < y < z) # Output: True

# Define some strings
a = "apple"
b = "banana"
c = "cherry"

# Check if a is less than b (alphabetical order)
print(a < b) # Output: True

# Check if b is not equal to c
print(b != c) # Output: True

# Check if a is greater than or equal to c
print(a >= c) # Output: False


#Logical operators are used to combine conditional statements and return a boolean value (True or False)

a = 10
b = 5
c = 0
print(a > 0 and b > 0) # True
print(a > 0 and c > 0) # False

# arithmetic operators
a = 7
b = 2
print('Sum: ', a + b) # addition
print('Subtraction: ', a - b) # subtraction
print('Multiplication: ', a * b) # multiplication
print('Division: ', a / b) # division
print('Floor Division: ', a // b) # floor division
print('Modulo: ', a % b) # modulo
print('Power: ', a ** b) # power

# assignment operators
x = 5 # assign 5 to x
x += 3 # add 3 to x and assign the result to x
x -= 2 # subtract 2 from x and assign the result to x
x *= 4 # multiply x by 4 and assign the result to x
x /= 2 # divide x by 2 and assign the result to x

# comparison operators
y = 10
z = 8
print('y == z =', y == z) # equal to
print('y != z =', y != z) # not equal to
print('y > z =', y > z) # greater than
print('y < z =', y < z) # less than
print('y >= z =', y >= z) # greater than or equal to
print('y <= z =', y <= z) # less than or equal to

# logical operators
a = True
b = False
print('a and b =', a and b) # logical and
print('a or b =', a or b) # logical or
print('not a =', not a) # logical not


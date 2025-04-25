# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and stops before a specified number.


#The range() function returns a range object which is a sequence of numbers. 
#We can see what is inside this object by converting it to other types like list.
# Using range to generate a sequence of numbers
result = range(1, 11)

# Converting the range to a list
result = list(result)

# Now 'result' is a list
print(result)


#Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
x = range(3, 20, 2)
for n in x:
  print(n)

# Since range() generates a sequence of numbers, 
# it is commonly used with for loops to iterate over the loop a certain number of times.
for values in range(1, 11):
  print(values, "i am blessed")

  # In this case, range(2, 11, 2) generates a sequence of even numbers starting from 2, 
  # up to (but not including) 11, with a step size of 2. The output will be:
  # Using range to print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)


    # Using range to print numbers from 0 to 4
for i in range(5):
    print(i)


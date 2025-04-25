#Strings: Are sequences of character data.A string is a sequence of characters or textual data. 
#In Python, we create strings by enclosing characters inside quotations. 
#String are immutable(this means they can not be changed after creation)
#can only concatenate str


# creating a strings
fruit = "watermalon"
print(f"List all the fruit: {fruit}")

# access the first item of a string
print(f"Access the first fruit: {fruit[0]}")

# access the last item of a string using a negative indexing
print(f"Access the last fruit: {fruit[-1]}")

# access item using slice
print(f"access item using slice {fruit[1:4]}")

# first to fourth items
print(f"first to fourth items {fruit[:4]}")

# from third to last item
print(f"from third to last item {fruit[2:]}")

# We use the asterisk * operator to repeat a string a certain number of times:
new_fruit= fruit *3
print(new_fruit)

# A string containing multiple words separated by spaces.The split() method is used here.so it splits the string into a list of words wherever there is a space.
fruit = "apple banana apple orange banana apple"
fruit_list = fruit.split()
print(fruit_list)

#count how mant time an item appears
fruit = "watermalon"
new_fruit= fruit.count('w')
print(new_fruit)

#concatenate strings
fruit= "watermalon"
new_fruit= "apple"
result= fruit +" "+ new_fruit
print(result)


# Iterating through a String
for new_fruit in fruit:
    print(f"iterate over the items {new_fruit}")

# find length of a string
new_fruit= len(fruit)
print(f"to know the length {new_fruit}")


# We can also use the in operator to find out if a substring is not in a given string
print("w" not in {fruit})
# We can also use the in operator to find out if a substring is present in a given string
print("w" in {fruit})

# To delete a specific item from a tuple, you can convert it to a list, modify it, and then convert it back to a tuple.
fruit_list = list(fruit)
fruit_list.remove('grape')
fruit = tuple(fruit_list)

print(f"Delete 'grape' from the list: {fruit}")

# This will print the index where "m" starts in "watermelon"
fruit = "watermelon"
index = fruit.find("m")
print(index) 

 # This will print the index where 'r' is found
fruit = "watermelon"
index = fruit.index('r')
print(index)

# for loop
fruit = "watermalon"
for result in fruit:
 print(result)

 #while loop. in a FUNCTION block
 def kind_of_fruits(name):
  fruit = "watermalon"
 while True:
  if "w" in fruit:
   print("yes")
   break
  else:
   print("no")

kind_of_fruits("sweet")

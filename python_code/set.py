# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members

# create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)


# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#we can add a single element using the add method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# delete items
thisset.remove("apple")
print(thisset)

# we can add multiple elements using update method.The update method can take tuples,lists,strings or other
#as its argument.
thisset = {6, 7, 8}
thisset.update([1,2,3,4,5])
print(thisset)

thisset = {"red", "green", "blue"}
thisset.update(["yellow", "purple"])
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["coconut", "mango","2"])
print(thisset)

# remove to set
thisset = {"apple", "banana", "cherry","orange"}
thisset.remove("orange")
print(thisset)


# iterate through items of a set by using a for loop
thisset = {'apple', 'banana', 'orange', 'pear'}
for fruit in thisset:
    print(fruit)

#check if an item is in a set or not by using the in keyword
thisset = {'apple', 'banana', 'orange', 'pear'}
print('apple' in thisset)

#check if an item is in a set or not by using the not in keyword
thisset = {'apple', 'banana', 'orange', 'pear'}
print('apple' not in thisset)




# You can't access elements in a set using indexing like you do with lists.
# Instead, you can use a loop or convert the set to a list.
# Here's an example of how to convert the set to a list and access the first item:
thisset = {"apple", "banana", "cherry"}
thisset_list = list(thisset)
print(f"access the first item: {thisset_list[0]}")



# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# A set with strings, integers and boolean values:
thisset = {"abc", 34, True, 40, "male"}
print(thisset)

#using conditional statement 
thisset = {"apple", "banana", "cherry"}
if "apple" in thisset:
    print("yes")
else:
    print("no")


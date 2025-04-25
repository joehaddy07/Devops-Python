#List literals are written within square brackets [ ]. 
#We create lists by placing items inside square brackets [] separated by commas.
#A list can contain mixed data type as well as duplicate elements.

"""Create a list of AWS services and modify the list appropriately."""
def main():

# Create a list of AWS services.
 aws_services = ['ec2', 'lambda', 's3', 'RDS', 'DynamoDB']
 print(f" AWS services list: {aws_services}")


#Access the first service in the list
 first_services = aws_services[0]
 print(f" first services: {first_services}")


#Access the last services in the list
 last_service = aws_services[-1]
 print(f" last service is access: {last_service}")


#modify the last service in the list
 aws_services[-1] = 'SNS'
 print(f" last service is modified: {aws_services}")


 #add service
 new_service = aws_services.append('sg')
 print(f" add service: {aws_services}")


#insert put ebs in a specified location which is between s3 and RDS
 new_item = 'ebs'
 insert_location = 2  # You need to specify the location (index) where you want to insert 'ebs'
 aws_services.insert(insert_location, new_item)
 print(f" put new service in a specified: {aws_services}")

 # pop remove service from list
 new_service = aws_services.pop(2)
 print(f" remove service in the list: {aws_services}")

# remove service from list but you have to specified the service
 new_service = aws_services.remove('ec2')
 print(f" remove specified service: {aws_services}")

 #count occurrences of an element in the list, like "apple"
 count_of_apples = fruits.count("apple")  # This returns 1
 print(count_of_apples)  # This prints 1


 # count return the number of times the value appears in the list
 new_service = aws_services.count(3)
 print(f" return the number of time the value appears: {aws_services}")

 #to know the lenght of a list
 new_service = len(aws_services)
 print(f" to know the lenght of a list: {new_service}")

 #reverse the list
 new_service = aws_services.reverse()
 print(f" reverse the list: {aws_services}")


if __name__ == '__main__':
    main()




fruits = ["apple", "banana", "orange","watermalon"]

# access the first item on the list
new = fruits[0]
print(f"acces first fruit: {new}")

# access the last item on the list
new = fruits[3]
print(f"access last fruit: {new}")

# add items to the list
fruits.append("coconut")
print(f"added fruit:{fruits}")

# delete items from the list
fruits.remove("banana")
print(f"remove fruit: {fruits}")

# reverse the list
fruits.reverse()
print(f"reverse fruit list: {fruits}")

#copy the list
new = fruits.copy()
print(f"Original list of fruits: {fruits}")
print(f"Copied list of fruits: {new}")

# count how many times an item appears in the list
new = fruits.count("apple")
print(f"how many times does apple appear on the list: {new}")

# A string containing multiple words separated by spaces.The split() method is used here.so it splits the string into a list of words wherever there is a space.
sentence = "apple banana apple orange banana apple"
words = sentence.split()
print(words)

# List of Lists (Nested Lists):You can have lists inside lists.
# A 2D list (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
print(matrix[0][1])  # Output: 2 (second element of the first list)

# Combining Lists:You can concatenate lists using the + operator or extend an existing list using extend().
# Concatenating two lists
more_fruits = ['grape', 'melon']
combined = fruits + more_fruits
print(combined)  # Output: ['apple', 'cherry', 'grape', 'melon']

# Extending an existing list
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'cherry', 'grape', 'melon']





# extend the list
fruits = ["apple", "banana", "orange","watermalon"]
fruits.extend(["mango", "sugarcane"])
print(fruits)

#using in OPERATOR to check the value
print("apple" in fruits)

#using not in OPERATOR to check the value
print("apple" not in fruits)

# Insert "mango" at index 2
fruits.insert(2, "mango")  
print(f"Updated list: {fruits}")

# to sort the complete list
new = fruits.sort()
print(f"sort the list: {fruits}")

# to know the lenght of the list
new = len(fruits)
print(f"to know the lenght of the list: {fruits}")


# to clear the list means to empty the list
new = fruits.clear()
print(f"to clear the list:{fruits}")

# to know the index of apple
fruits = ["apple", "banana", "orange", "watermelon", "coconut"]
index_of_apple = fruits.index("apple")
print("Index of 'apple':", index_of_apple)


# Removes the element at index 0 ("apple") it remove the item which is specified
fruits = ["apple", "banana", "orange", "watermelon", "coconut"]
removed_fruit = fruits.pop(0)  
print("Removed fruit:", removed_fruit)
print(fruits)

#If you want to find the index of a specific fruit
index_of_banana = fruits.index("banana")
print(index_of_banana)

#copy list
fruits = ["apple", "banana", "orange","watermalon"]
fruits_copy =fruits.copy()
print(fruits_copy)

#using conditional statement
if "apple" in fruits:
    print("yes")
else:
    print("no")

#for loop
fruits = ["apple", "banana", "orange","watermalon"]
for fruits_loop in fruits:
    print(fruits_loop)

#why loop
fruits = ["apple", "banana", "orange", "watermelon"]
while True:
    if "apple" in fruits:
        print("yes")
        break
    else:
        print("no")

#function(block of organized and reusable code)
def details(values):

 fruits = ["apple", "banana", "orange", "watermelon"]
 while True:
    if "apple" in fruits:
        print("yes")
        break
    else:
        print("no")

details('result')

# A list containing a list that contains a dictionary. The code is iterating through a nested list structure. 
# gets the value associated with the key 'Name' from the dictionary, which is 'Sammy'
person = [[{'Name': 'Sammy','Salary': 1000000,'Age': 40,'Address': 'limbe','Job': 'IT','Car': 'Toyota'}]]
for item in person:
  for item1 in item:
   print(item1.get('Name'))

# A list containing another list.  iterates through the outer list, so item becomes the inner
fruits = [["apple", "banana", "orange","watermalon"]]
for item in fruits:
    print(item[2])





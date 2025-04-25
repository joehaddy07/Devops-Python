#A dictionary consists of a collection of key-value pairs. 
#Each key-value pair maps the key to its associated value.
#You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). 
#A colon (:) separates each key from its associated value:

haddison={ 'abo': 1,
           'david': 2,
           'suki': 3,
           'caro' : 4,
           'abel' : 5,
          
          }


#access abel
family = haddison['abel']
print(f"Family tree:{family}")

#modified
haddison ['david']= "1"
print(f"Update family tree:{haddison}")

#add
haddison['james'] = "6"
print(f"\nAdded james: {haddison['james']}")

del haddison['david']
print(f"\nRemoved david: {haddison}")

#displaying different aspect of dictionary
print(haddison.keys())
print(haddison.values())
print(haddison.items())


#Dictionaries are versatile and widely used in Python for various tasks.
# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
new = my_dict['name']
print(f"access the name:{new}")

# Modifying a value
new= my_dict['age'] = 26
print(f"modify the list: {new}")

# Adding a new key-value pair
my_dict['school'] = 'ombe'
print(f"\nAdded school:{my_dict['school']}")

# remove item
del my_dict['city']
print(f"delete item: {my_dict}")

# Iterating through keys, item and values
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


#access the first item using get.
person = {'Name': 'sammy', 'Age': 40, 'Address': 'limbe'}
new_person = person.get('Name')
print(f"Access the first item: {new_person}")

#access if a key exist using in
person = {'Name': 'sammy', 'Age': 40, 'Address': 'limbe'}
print('Name' in person)

#access if a key don't exist using not in
person = {'Name': 'sammy', 'Age': 40, 'Address': 'limbe'}
print('salary'not in person)

    
print(f"access the first item: {person['Name']}")

person['Age']=39
print(f"modify age: {person}")

person['Food']='Rice'
print(f"add new item: {person}")

del person['Job']
print(f"delete item: {person}")



person = {
    'Name': 'Sammy',
    'Salary': 1000000,
    'Age': 40,
    'Address': 'limbe',
    'Job': 'IT',
    'Car': 'Toyota'
}

  # access the first item  
print(f"access the first item: {person['Name']}")

# access the first item
print(person.get('Name'))

person['Age']=39
print(f"modify age: {person}")

person['Food']='Rice'
print(f"add new item: {person}")

del person['Job']
print(f"delete item: {person}")

# Iterating over the dictionary to find the 'Job' key
for key, value in person.items():
    if key == 'Job':
        print(f"Job: {value}")



print(person.keys())
print(person.values())
print(person.items())

# Using a Dictionary to Count Occurrences:Let's count the occurrences of each word in a sentence.

sentence = "apple banana apple orange banana apple"
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)  
# Output: {'apple': 3, 'banana': 2, 'orange': 1}




# 1. Define the sentence
sentence = "apple banana apple orange banana apple"

# 2. Split the sentence into individual words, creating a list of words
words = sentence.split()  
# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 3. Initialize an empty dictionary to store word counts
word_count = {}

# 4. Loop through each word in the list 'words'
for word in words:
    # 5. Check if the word already exists as a key in the dictionary
    if word in word_count:
        # 6. If the word exists, increment its count by 1
        word_count[word] += 1
    else:
        # 7. If the word doesn't exist, add it to the dictionary with a count of 1
        word_count[word] = 1

# 8. Print the word count dictionary after processing all the words
print(word_count)


# Dictionary with List Values:You can have lists as dictionary values.
phone_book = {
    'Alice': ['123-456-7890', 'alice@example.com'],
    'Bob': ['987-654-3210', 'bob@example.com']
}

print(phone_book['Bob'][0])  # 987-654-3210

 # Nested Dictionaries:You can store dictionaries within dictionaries.
employees = {
    'emp1': {'name': 'Alice', 'age': 30, 'position': 'Engineer'},
    'emp2': {'name': 'Bob', 'age': 25, 'position': 'Designer'}
}

print(employees['emp1']['name'])  # Alice

# A list containing a list that contains a dictionary. The code is iterating through a nested list structure. 
# gets the value associated with the key 'Name' from the dictionary, which is 'Sammy'
person = [[{'Name': 'Sammy','Salary': 1000000,'Age': 40,'Address': 'limbe','Job': 'IT','Car': 'Toyota'}]]
for item in person:
  for item1 in item:
   print(item1.get('Name'))







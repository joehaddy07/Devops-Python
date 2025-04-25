#In Python, both for and while loops are used for repetitive execution of code, but they have different purposes and syntax.

#for Loop:
#A for loop is typically used when you know in advance how many times you want to iterate, 
#especially when you want to iterate over a collection of items like a list, tuple, string, or range.

#The loop iterates over each item in the collection, and you don't have to manually manage the iteration variable.
#The for loop uses the in keyword to iterate over elements, making it convenient for iterating through sequences.

for i in range(5):  # Loop from 0 to 4
    #print(i)

    details = ('banana', 'apple', 'watermelon', 'orange')

for _ in range(11):
    for detail in details:
        print(detail)


    details = ('banana', 'apple', 'watermelon', 'orange')

for detail in details:
    print(detail)


    for had in (1,2,3,4,5): # The loop iterates over each item in the collection
     print(had)

for had in (1,2,3,4,5):
 for hadd in ('a','b','c','d','e',): # The loop iterates over the both item in the collection 
   print(hadd,had)


   details = ('banana','apple','watermalon','orange')
for detail in details:
    print(f"name the fruits in the list: {details}")

   #create a simple multiplication table using a Python loop
mango = 9
for details in range(1, 13):
    product = mango * details
    print(mango, "*", details, "=", product)


#while Loop:
#A while loop is used when you want to execute a block of code repeatedly as long as a certain condition is true.
#You may not know in advance how many iterations will be needed, and 
#it's important to define a condition that, when false, will terminate the loop.
#You manually manage the loop condition and the iteration variable.


#while test_condition:
    #statement(s)

# the code will run when the test condition is true and the code stop running when the test
#condition is false.
count = 0
while count < 5:  #test_condition
    print("i am blessed.")#statement(s)
    count = count + 1  # Increment the counter   


# Here, the test condition is never False, so the loop runs forever until the system's memory runs out. 
count = 0
while count < 5:
    print("I am inside a loop.")
    print("Looping is interesting.")





# the loop will run as long as sam is less than joe, and with each iteration of the loop, 
# the value of sam is incremented by 1. Once sam becomes equal to or greater than joe, the loop will terminate. 
# in other words the code will run when the test condition is true and the code stop running when the test
#condition is false.

sam = 4
joe = 6

while sam < joe:
  print("blessed.")
  sam = sam + 1           




#In Python, a function is a block of organized, reusable code that is used to perform a specific task or a set of tasks. 
#Functions provide a way to modularize and structure your code, 
#making it more organized, easier to read, and allowing for code reuse.

def function_name(parameters):
    # Function code
    # ...
  return ("result")





def greet(name):
    print("Hello", name)
    print("How do you do?")

greet("Jack")


#The code you provided defines a function called detail that takes two parameters, name and age. Inside the function, 
#it prints a message that includes the word "blessed," the name parameter, and the number 42. 
#Then, you call the detail function with the arguments "haddison" and 42.
#So, when you call detail("haddison", 42), it will print the following message:

def detail(name, age):
 print("i am blessed", name , 42)


detail("haddison", 42)


def details(value):
    x = 10
    y = 20
    result = x + y
    print("find value", result)

details("answer")

def fruits(banana, orange, car, apple):
    result = int(banana) * int(apple)  # Convert string inputs to integers
    if result == 730:
        print(f"pass: {result}")
    else:
        print(f"fail: {result}")

# Call the function with numerical arguments
fruits(10, 42, 37, 73)

#CONDITIONAL STATEMENTS
#A piece of code that executes instructions base on a particular state useful for:
#(1) Controlling the flow of a program
#(2)Executing different code based on different condition.

#if condition meaning: Code to be executed if the condition is True
#else condition meaning: Code to be executed if the condition is False

#if condition1:
    # Code to be executed if condition1 is true
#elif condition2:
    # Code to be executed if condition2 is true
#elif condition3:
    # Code to be executed if condition3 is true
#else:
    # Code to be executed if none of the conditions are true

    

"""determine the condition"""
#Example 1: Checking if a string contains a certain character

#In this example, we use the in operator to check if the character 'key' is present in the string string. 
# If it is, the condition 'key' in string is True, and the code block indented below the if statement will be executed, 
# printing the message "The string contains the character" followed by the character itself.

#If 'key' is not present in string, the condition is False, and the code block indented below the else statement will be executed, 
# printing the message "The string does not contain the character" followed by the character itself.


def main():
 
 #to know if the grand kids of haddison's family are eligible to vote.
 
 oldest_kid = 18 # You can change this value. the top value is been compare with the below value. 

 if oldest_kid >= 17:
  print(f"you are eligible to vote")
 else:
   print(f"you are not eligible to vote")

   #In this example, we use the if statement to check if the value of the age variable is greater than or equal to 18. 
   #If it is, we print the string "You are eligible to vote." Otherwise, we print the string "You are not eligible to vote."
   #The f in front of the string literal indicates that it is an f-string. F-strings allow us to embed expressions in strings. 
   #In this case, we are embedding the value of the age variable in the string.


#In this example, we use an if-elif-else statement to assign a letter grade based on a numerical score.
#The if statement checks if the score is greater than or equal to 90. If it is, the grade is set to "A".
#If not, the first elif statement checks if the score is greater than or equal to 80. If it is, the grade is set to "B". 
# If not, the second elif statement checks if the score is greater than or equal to 70, and so on. 
# If none of the conditions are met, the else statement assigns the grade "F".


score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
    
if __name__ == '__main__':
    main()



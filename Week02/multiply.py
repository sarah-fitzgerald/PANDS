# This allows you to multiply sums
# Author: Sarah Fitzgerald

# Function to multiply two numbers
# Reference: https://www.codegrepper.com/code-examples/delphi/make+a+calculator+on+python+vs+code

def miltiply (num1, num2) :
    return num1 * num2

    print ("Please selection operation -\n" \
        "1. Multiple\n" )

#This section takes an input from a user

number_1 = int(input("Enter first number: " ))
number_2 = int(input("Enter second number: " ))

print(number_1, "*", number_2, "=", 
miltiply(number_1, number_2))

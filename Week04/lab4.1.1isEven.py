#Askes user to input number, then tell user is number is even or odd    
#Author: Sarah Fitzgerald

#Ask uset to input number
number = int(input("Please enter a number: "))


#If the number the user inputs is an even number then the program will print the number and a statment
if (number % 2) == 0:
        print ("{} is an even number".format(number))

#If the user inputs an odd number then the program will print the number and a statement
else:
    print("{} is an odd number".format(number))

    print (number)
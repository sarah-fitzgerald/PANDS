#This program asks user to guess a number and continue to prompt user until user gets the number right
#Author: Sarah Fitzgerald

number = 30

guess = int(input("Please guess the number: "))

while guess != number:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", number)
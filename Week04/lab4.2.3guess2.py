#This program asks user to guess a number and continue to prompt user until user gets the number right
    #Will let user know if the number is too high or too low
#Author: Sarah Fitzgerald

number = 30

guess = int(input("Please guess the number: "))

while guess != number:
        if number > guess:
            print ("Too low")
        elif number < guess:
            print ("Too high")
        guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", number)
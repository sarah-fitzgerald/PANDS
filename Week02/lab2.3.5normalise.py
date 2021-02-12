#Lab 2.3.5 Variables and State
#Reads in a string and strips any leading or trailing spaces
#Should also convert string to lower case
#Author: Sarah Fitzgerald

x = input ("Please enter a string: ")
y = x.strip() .lower()

a = len (x)
b = len (y)

print ("The normalised String is: " .format(y))
print ("We reduce the input string from {} to {} characters" .format (a, b))
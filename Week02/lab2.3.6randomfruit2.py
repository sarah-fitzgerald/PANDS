#Lab 2.3.6 Variables and State 
#Prints out random fruit, changes square brackets to rounds ones
#Author: Sarah Fitzgerald

import random

#List of fruits
fruits = ('Apple', 'Banana', 'Orange', 'Pear')

#Finds a random number between 0 and lenght-1
index = random.randint(0, len (fruits) - 1)

fruit = fruits[index]
print ("A random fruit: {}".format(fruit))
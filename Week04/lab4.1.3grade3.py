##This reads in a student precentage mark and outputs the grade
    #It will also round a decimal grade up or down to the nearest whole number
#Author: Sarah Fitzgerald

#Asks user to input their percentage grade into the program
grade = round(input("Please enter percentage grade: "))

#If the percentageis less than 40%
if (grade < 40): 
    print ("Fail")

#If the percentage is between 40% and 49%
elif (grade < 50):
    print ("Pass")

#If the percentage is between 50% and 59%
elif (grade < 60):
    print ("Merit 2")

##If the percentage is between 60% and 69%
elif (grade < 70):
    print ("Merit 2")

#If it is anything else above 70%
else:
    print ("Distincition")

print (grade)
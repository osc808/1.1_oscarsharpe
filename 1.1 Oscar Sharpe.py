'''
    author: Oscar Sharpe
    version: 1
    date: 25/08/2025
    description: A fitness tracker program to track a year 11 senior class and their workout results
'''

#----------libraries--------------
import random


#----------functions--------------
def main():
    pushups_per_day = [ ]    #Empty list that will have inputs added for the amount of pushups they were able to do

    while (True):               #Loop will loop until broken, which happens when the name is validated
        try:                    #Try/except 
            name = input('Please enter your name: ')        #String input asking for the users name
            if(len(name)>= 2 and len(name)<=20 and name.isalpha):   #Checks that the name length is more or equal to 2, and no longer than 20. It also checks that the input is a word and not a number
                break                                #The loop will break and the code will carry on if the name is validated               
            else:                                    #Else for if the input was not valid
                print('That was not a valid input')
        except:
            print('That was not a valid input')

    print(f'Hello {name}, welcome to the fitness tracker!')

    while (True):           #Loop that will loop until broken and age is validated
        try:                #Try/except
            age = int(input('Please enter your age: '))     #Int input asking for the users age
            if(age >=13 and age<=20 and age.is_integer):    #Checks that the age is an integer, and that it is in the range of 13-20 (Since it is a year 11 class)
                break       #Loop will break if the input is valid
            else:
                print('That was not a valid input')     #Error message will print if the input was not valid
        except:
            print('That was not a valid input')

    
    day_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday']  #List for the days of the week
    for days in day_of_week:
        while (True):
            try:
                print(days)                         #Prints each day of the week for each time it loops e.g. first loop will say 'Monday' and second will say 'Tuesday'
                user_pushups = (int(input('How many pushups were you able to do throughout the day?: ')))
                if(user_pushups >=0 and user_pushups <=100):
                    pushups_per_day.append(user_pushups)
                    break
                else:
                    print('That was not a valid input') #Code will repeat if invalid
            except:
                print('That was not a valid input') #Code will repeat if invalid
                
    print(f'Your scores across the day were {pushups_per_day}') #Tells the user their score across the 5 days
    top_score = max(pushups_per_day)        #Calculating the top score 
    print(f'Nice work! The most amount of pushups you did in one day was {top_score}')



        

#---------main routine------------
main()





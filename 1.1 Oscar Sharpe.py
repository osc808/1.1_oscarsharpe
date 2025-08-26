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
    pushups_per_min = [ ]    #Empty list that will have inputs added for the amount of pushups they were able to do
    while (True):               #Loop will loop until broken, which happens when the name is validated
        try:                    #Try/except 
            name = input('Please enter your name: ')        #String input asking for the users name
            if(len(name)>= 2 and len(name)<=20 and name.isalpha):   #Checks that the name length is more or equal to 2, and no longer than 20. It also checks that the input is a word and not a number
                break                                #The loop will break and the code will carry on if the name is validated               
            else:                                    #Else for if the input was not valid
                print('That was not a valid input')
        except:
            print('That was not a valid input')


    age = int(input('Please enter your age: '))     #Int input asking for the users age
    day_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday']  #List for the days of the week
    for i in day_of_week:
        pushups_per_min.append(int(input('How many pushups were you able to do: ')))

#---------main routine------------
main()





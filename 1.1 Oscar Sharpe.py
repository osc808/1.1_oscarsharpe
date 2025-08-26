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
    pushups_per_min = [ ]                           #Empty list that will have inputs added for the amount of pushups they were able to do
    name = input('Please enter your name: ')        #String input asking for the users name
    age = int(input('Please enter your age: '))     #Int input asking for the users age
    day_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday']  #List for the days of the week
    for i in day_of_week:
        pushups_per_min.append(int(input('How many pushups were you able to do: ')))

#---------main routine------------
main()





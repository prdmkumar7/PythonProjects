#importing module for random number generation
import random

#range of the values of a dice
min_val = 1
max_val = 6

#to loop the rolling through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Value is :")
    
    #generating and printing random integer from 1 to 6
    number = random.randint(min_val, max_val)
    print(number)
    if number==6:
        roll_again="yes"
        continue


    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again? :") 
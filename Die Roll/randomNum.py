import random;

#Program is a loop that restarts if the user decides to run the program again
#First program in python designed to learn loops, variables, and general syntax

while True:
    print("This program is designed to roll a die and return the value that is rolled \n")
    min = int(input("Enter a min "));
    if min <= 0:
        print("The min must be greater than 0. Min will now be 1");
        min = 1;
    max = int(input("Enter a max "));
    if max <= min:
        print("The max value cannot be less than/equal to the min. Max is now 10");
        max = 10;


    while True:
        answer = input("Would you like to run again? (y/n)" );
        if answer in('y', 'n'):
            break;
            print("Invalid Input");
    if answer == 'y':
        continue;
    else:
        print("Thank you for playing ");
        break;



import random;

def defaultChoices(min, max):
    #guessList = [ ];
    result = random.randint(min, max);
    while True:
        print("Please guess a number in the range of ", min, " to ", max, "\n");
        guess = int(input());
        if guess > result:
            print("You have guessed too high! Try again\n");
            #guessList.append(guess);
        elif guess < result:
            print("You have guessed too low! Try again\n");
        else:
            print("You have guessed correctly!\n");
            break;
    #print("Your guesses were \n");
    #for x in range(len(guessList)):
        #print(guessList[x]);
    return result;


while True:
    answer = int(input("The following game will test your guessing skills.\n"
        "The computer will pick a number and it is your job to guess what it is.\n"
         "Make a choice below:\n"
         "1. Easy (The numbers will be between 1 and 100\n"
         "2. Medium (The numbers will be between 1 and 1000)\n"
         "3. Hard (The numbers will be between 1 and 100000)\n"
         "4. Pick your own range (The numbers will be between 1 and a number of your choosing) \n"));

    if answer is 1:
        defaultChoices(1, 100);
        break;
    elif answer is 2:
        defaultChoices(1, 1000);
        break;
    elif answer is 3:
        defaultChoices(100000);
        break;
    elif answer is 4:
        userMin = int(input("Enter a min of your choosing \n"));
        if userMin < 1:
            print("Min cannot be less than 1! Min will now be 1 \n");
            userMin = 1;
        userMax = int(input("Enter a max of your choosing \n"));
        if userMax < userMin:
            print("Max cannot be less than the min. Min will now be 100 \n");
            userMax = 100;
        defaultChoices(userMin, userMax);
        break;
    else:
        print("Invalid response \n");
        break;
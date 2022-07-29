import random # importing random module
import checkingNum # importing file called checkingNum.py

def main():
    randNum = random.randint(1, 100) # generate random number between 1 and 100
    runGame = True # keeps game running
    numInput = 0 # number inputted
    tries = 0 # counts number of tries

    print("Random number between 1 and 100 has been generated.\nYou have 7 tries to guess the correct number.\nEnter 999 to exit at any time.")
    numInput = int(input("\nWhat's your first guess? ")) # prompt user and get num

    while runGame == True: # only 5 tries allowed
        check = checkingNum.checkInput(randNum, numInput) # import function from checkingNum.py

        if tries == 5: # python counts like: 0, 1, 2, 3, 4, 5, 6
            print("This is your last attempt.")

        if check == 999 or tries == 6: # end game
            runGame = False

        else: # end game not inputted
            numInput = int(input("Please enter your new guess: "))
            tries += 1 # increase by one
    
    checkingNum.endMsg(tries, randNum, numInput) # import function from checkingNum.py --> display end message if user runs out of tries.

main() # call main function (Note: not necessary but done anyways - see reason here: https://stackoverflow.com/questions/4041238/why-use-def-main )

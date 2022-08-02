import random # importing random module
#import checkingNum # importing file called checkingNum.py
from checkingNum import check_num

def main(): #Fill in the blank lines inside the function, be sure to delete pass
    runGame = True # keeps game running
    tries = 0
    number_generated = random.randint(1, 100)
    while runGame == True: # only 7 tries allowed
        number_inputed = int(input("Enter your number: "))
        if number_generated == number_inputed:
            print("You guessed the number!")
            break
        
        output = check_num(number_inputed, number_generated)
        print(output)
        tries += 1
        if tries == 7:
            print("You did not get the number :(")
            break
        


main() # call main function (Note: not necessary but done anyways - see reason here: https://stackoverflow.com/questions/4041238/why-use-def-main )

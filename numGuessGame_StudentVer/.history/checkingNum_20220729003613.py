def checkInput(randNum, numInput): # checking user input
    if numInput == 999: # end game selected
        return 999

    if numInput == randNum:
        print("\nCongrats! You have guessed correctly.")
        numInput = int(input("Type '999' to exit. ")) # prompt user and get num
        return 999

    if numInput > randNum: # guess is higher than random num
        print("Too high!")
        return # returns None

    if numInput < randNum: #guess is lower than random num
        print("Too low!")
        return # returns None 

def endMsg(tries, randNum, numInput): # ending message
    if tries == 6 and (numInput != randNum): # no more tries and user is still wrong
        print("\nSorry, you ran out of tries.")
        print("Random number: ", randNum) # dsiplay answer


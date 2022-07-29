import programFunctions # importing file that holds program functions

def main():
    runProgram = True # boolean
    print("Welcome.") # welcom messages displayed in terminal

    while runProgram == True: # while loop keeps program running
        option = int(input("Select:\n1 - View all items\n2 - Remove an item\n3 - Add an item\n4 - Change an item\n5 - Create CSV file\n6 - Exit program\n")) # gets user input
        
        if option == 6: # if 6 selected, end program
            return # returns out of main()
        
        programFunctions.getOption(option) # calls getOption from programFunctions.py
        
main() # calling main function
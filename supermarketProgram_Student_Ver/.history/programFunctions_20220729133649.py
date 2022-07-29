import pandas as pd # import pandas libary but allow for using 'pd' when referring to it in the code --> needed for CSV file function
from itemsInShop import inventory # importing dictionary called inventory from itemsInShop.py

def getOption(option): # gets the user's option selection and "directs" the flow of the code accordingly
    if option == 1: # option 1: view item
        viewInventory() # calls viewInventory function
    if option == 2: # option 2: remove item
        key = str(input("Which item would you like to remove? ")).lower() # prompts user through message in terminal, gets user input as a string, and changes input to lowercase
        removeItem(key) # calls removeItem function
    if option == 3: # option 3: add item
        addItem() # calls addItem function   
    if option == 4: # option 4: change item
        changeItem() # calls changeItem function
    if option == 5: # option 5: convert to CSV
        getCSV() # calls get CSV function
    # option 6 is dealt with in main()
    elif option not in [1, 2, 3, 4, 5, 6]: # error-checking
        print("That was not an option. Please choose again.\n")

def viewInventory(): # Part 2: Write your function here, and delete pass
    pass


def addItem(): 
    item = str(input("What food/item would you like to add? ")) # prompt user in terminal and get input as a string
    #Ensure no duplicates
    if item in inventory.keys(): # no duplicates
        print("This item already exists.\n")
        return # end function

    # Part 3: write your function here
    #Create a new dictionary
    #Ask the user on the item's info on price, in stock status, and discount


    viewInventory() # print updated inventory

def removeItem(key): # Part 4: Write your function here, and delete pass
    pass 

def changeItem(): # declaring function
    key = str(input("Which item would you like to change? ")) # prompt user and get the item name as a string and store it in 'key'

    while key not in inventory.keys(): # do while loop not avaliable in python so use above prompt first then use while loop
        key = str(input("Item doesn't exist. Enter again please: ")) # item is not in keys() list so prompt and get string again

    part = str(input("Would you like to change price/inStock/discount? " )) # part is the part of the information to be changed

    if part == "price": # if the part to be changed is "price"
        inventory[key][part] = float(input("Enter the new price: "))  # prompt and get float --> store this in the correct key:value pair

    elif part == "inStock":
        newStockStatus = str(input("Enter True or False: ")).lower() # prompt and get str --> store this in the correct key:value pair
        if newStockStatus == "true": # lowercase because we used lower() to ensure input wis always lower
            inventory[key][part] = True # boolean data type
        else:
            inventory[key][part] = False # boolean data type

    elif part == "discount":
        newDiscount = str(input("Enter the percentage discount: ")).lower() # get new discount: str
        if newDiscount[-1] == "%": # if the % was entered, input that new entery
            inventory[key][part] = newDiscount # updating the index's key's value
        else:
            inventory[key][part] = newDiscount + "%" # add '%' sign if the user didn't add it

    else: # part inputted doesn't exist
        print("This attribute doesn't exist.\n")
        return
    
    viewInventory() # print updated inventory

def getCSV(): # declaring function
    df = pd.DataFrame.from_dict(inventory) # create a data frame from the dictionary by calling pandas libary
    dfTransposed = df.T # transposing dataframe --> swap rows and columns for readability
    dfTransposed["discount"].fillna("0%", inplace = True) # if there are any blanks in the discounts row, fill it with 0%

    print("Converting dataframe to CSV.") # show message in terminal to let user know what's going on
    print(dfTransposed) # show dataframe in terminal
    df.to_csv("shopInventory.csv") # create CSV file using to_csv()
    print("CSV File Created.\n") # tell user file has been created
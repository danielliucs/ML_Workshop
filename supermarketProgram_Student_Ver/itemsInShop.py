# 'inventory' is a dictionary storing dictionaries of the items in the shop (dictionary of dictionaries)
# Dictionaries are made up of key:value pairs
# Dictionaries are a data structure type in Python

inventory = { # initializing and filling up the dictionary alled 'inventory'
    "apple": { # index of first dictionary is "apple"
        "price": 5.00, # key is "price", value is "5.00"
        "inStock": True,
        "discount": "20%"
    }, # end of first dictionary

    "orange": { # next dictionary with index of "orange"
        "price": 6.00, 
        "inStock": True, # key is "inStock", value is "true"
        "discount": None
    }, # end of second dictionary
    
    "banana": {
        "price": 4.32,
        "inStock": True,
        "discount": None
    },

    "lettuce": {
        "price": 1.97,
        "inStock": True,
        "discount": None
    },

    "cabbage": {
        "price": 7.11,
        "inStock": True,
        "discount": "10%"
    }
} # end of inventory dictionary

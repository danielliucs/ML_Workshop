#Write your functions on checking input here

def check_num(my_guess, actual_num):
    if my_guess < actual_num:
        return "Your guess is lower than the actual number"
    elif my_guess > actual_num:
        return "Your guess is higher than the actual number"
    else:
        return "You guessed the number!"
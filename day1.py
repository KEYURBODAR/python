## Prerequisites : print(), input(), strings , f-strings, if - else

# Brand Name Generator 

print("Welcome to the brand name generator!")
City = input("Which city are you based in?\n")
Food = input("What's the famous food in your city?\n")
print(f"Your brand name is {City} {Food}")

# A Number choosing game

print("Welcome to this Adventure Game!")
commands = input("Choose your mode : Easy, Medium or Hard\n" )
if commands == 'Easy':
    print("Easy mode enabled!")
    import random
    ask_user = input("Choose any number between 1-6\n")
    dice_roll = random.randint(1,6)
    if ask_user == dice_roll:
        print(f"Congrats! You won! The number is {ask_user}")
    else:
        print(f"You lose! The number was {dice_roll}")
elif commands == 'Hard':
    print("hard mode enabled!")
    import random
    import time
    start_time = time.time()
    ask_user1 = input("Choose any number between 1-20\nYou only have 5 seconds to guess otherwise you lose!\n")
    dice_roll1 = random.randint(1,20)
    end_time = time.time()
    time_taken = end_time - start_time
    if ask_user1 == dice_roll1:
       if time_taken <= 5:
           print(f"Congrats! you took {time_taken} seconds!")
       else:
           print(f"Your answer was correct! but you took {time_taken} seconds!")
    else:
        print(f"Incorrect! you took {time_taken} seconds and the answer is {dice_roll1}")
elif commands == 'Medium':
    print("Medium mode enabled!")
    import random
    import time
    start_time1 = time.time()
    ask_user2 = input("Choose any number between 1-10\nyou have only 10 seconds to guess!\n")
    dice_roll2 = random.randint(1,10)
    end_time1 = time.time()
    time_taken1 = end_time1 - start_time1
    if ask_user2 == dice_roll2:
        if time_taken1 <= 10:
            print(f"Congrats! You took {time_taken1} seconds!")
        else:
            print(f"Your answer was correct! but you took {time_taken1} seconds!")
    else:
        print(f"Incorrect! You took {time_taken1} seconds and the correct answer was {dice_roll2}")


# A simple calculator you can say in 3 lines of code

ask = input("Enter your expression: ")
result = eval(ask)
print("The result is ", result)

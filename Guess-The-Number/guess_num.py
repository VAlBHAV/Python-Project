
import random

num = random.randrange(0, 100)
guessCheck = "wrong"
print("--Welcome to Guess The Number Game--")

while guessCheck == "wrong":
    res = int(input("Please input a number between 0 and 100:"))
    try:
        val = int(res)
    except ValueError:
        print("This is not a valid integer. Please try again!")
        continue
    if val < num:
        print("This is lower than actual number. Please try again!")
    elif val > num:
        print("This is higher than actual number. Please try again!")
    else:
        print("Hurray! you won, this is the correct number.")
        guessCheck = "correct"
print("Thank you for playing Guess The Number. See you again!")

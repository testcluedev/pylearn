# Write a program for a simple guessing game. The program should randomly choose a number between 1 and 100, 
# and then ask the user to guess the number. 
# The program should tell the user if their guess is too high, too low, or correct.

# import random

# def guessing_game():
#     # Generate a random number between 1 and 100
#     number = random.randint(1, 100)
    
#     # Initialize the number of attempts
#     attempts = 0
    
#     while True:
#         # Increment the number of attempts
#         attempts += 1

#         # Get the user's guess
#         guess = int(input("Guess a number between 1 and 100: "))

#         # Check the guess against the number
#         if guess < number:
#             print("Too low!")
#         elif guess > number:
#             print("Too high!")
#         else:
#             print(f"Congratulations! You've guessed the number in {attempts} attempts.")
#             break

# # Start the game
# guessing_game()

import random
myrandom = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    myguess = int(input("Enter your guess: "))
    if myguess < myrandom:
        print("Too low!")
    elif myguess > myrandom:
        print("Too high!")
    else:
       print(f"You guessed it correctly, in {attempts} attempts")
       gamepoint = input("Enter C to continue or E to end the game: ")
       if gamepoint == "C":
           attempts = 0
           pass
       else:
           break



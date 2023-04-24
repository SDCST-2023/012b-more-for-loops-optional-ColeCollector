#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random


answer = random.randint(1,100)
number = int(input("Enter a number from 1 to 100: \n"))
guesses = 0

for i in range (1,10):
    if number != answer and guesses != 10:
        if number > answer:
            number = int(input("Too high, guess again. \n"))
            guesses = guesses+1
        
        else:
            number = int(input("Too low, guess again. \n"))
            guesses = guesses+1

        
    if number == answer:
        print("You guessed the number! It was", answer)
        break

    if guesses == 9 and number != answer:
        print("You Lost, you ran out of guesses. The answer was", answer)

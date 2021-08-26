#Guess the number
import random
print("Please Player 1 enter your name")
name1 = str(input())
print("please player 2 enter your name ")
name2 = str(input())
print("Please " + name1 +" select the number range start point")
player1_1 = int(input()) # This is the start of the number
print("Please " + name1 + " select the number range end")
player1_2 = int(input())
#selecting the number range
secretNumber = random.randint(player1_1,player1_2)
print("How many tries you want to give to the " + name2)
tries = int(input())
#Guessing the numbers
for i in range (1,tries):
    print("Make a guess")
    guess = int (input())

    if guess < secretNumber:
        print("Your guess is lower make a higher guess")
    elif guess > secretNumber:
        print("Your guess is higher make a lower guess")
    else:
        break
if guess == secretNumber:
    print("Good JOb you guessed the number in " + str(i) + " guesses")
else:
    print(name1 + "won The correct number is: " + str(secretNumber))
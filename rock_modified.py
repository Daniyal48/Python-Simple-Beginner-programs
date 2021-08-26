import random
import sys
# Setting up initital variables to zero
wins = 0
loss = 0
tie = 0
# Main Function
while True:
    print("%s wins, %s loss , %s tie" %(wins, loss, tie))
    #player input fucntion
    while True:
        print('Enter your Move \n R for Rock \n P for Paper \n S for Sicssor and \n Q to Quit the game')
        playermove = input()
        if playermove == 'q' or playermove == 'Q':
            print("You chose to quit Bye!!!!")
            sys.exit() # close the Program
        if playermove == 'r' or playermove == 'R' or playermove == 'p' or playermove == 'P' or playermove == 's' or playermove == 'S':
            break # Here the second while will be broken
    if playermove == 'r' or playermove == 'R':
        playermove = 'r'
        print("Rock versues.....")
    elif playermove == 'P' or playermove == 'P':
        playermove = 'p'
        print("Paper versues....")
    elif playermove == 'S' or playermove == 's':
        playermove = 's'
        print("Sicssors versues...")
    # Compter Moves
    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        computerMove = 'r'
        print("Rock")
    elif randomnumber == 2:
        computerMove = 'p'
        print("paper")
    elif randomnumber == 3:
        computerMove = 's'
        print("Sicssor")
    # Calculating the number of wins and losses for the player 
    if playermove == computerMove:
        print("Tie")
        print("########################")
        tie = tie + 1
    elif playermove == 'r' and computerMove == 's':
        print("You win")
        print("########################")
        wins = wins + 1
    elif playermove == 'p' and computerMove == 'r':
        print("You win")
        print("########################")
        wins = wins + 1
    elif playermove == 's' and computerMove == 'p':
        print("You win")
        print("########################")
        wins = wins + 1
    elif playermove == 'r' and computerMove == 'p':
        print("You lose")
        print("########################")
        loss = loss + 1
    elif playermove == 'p' and computerMove == 's':
        print("You lose")
        print("########################")
        loss = loss + 1
    elif playermove == 's' and computerMove == 'r':
        print("You lose")
        print("########################")
        loss = loss + 1

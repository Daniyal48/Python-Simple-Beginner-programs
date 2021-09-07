import sys
def collatz(num):                                #The collatz function
    while num !=1:                               # Loop which checks the number and stops until its one
        if num % 2 == 0:                         #for even number
            num = num // 2 
            return (num)
        elif num % 2 != 0:                       #for odd number you can also do == 1
            num = 3 * num + 1
            return (num)
#user_number = int(input("Please enter an integer number or 0,1 to close the program "))          # int data type
try:
    user_number = int(input("Please enter an integer number or 0,1 to close the program "))          # int data type
    while user_number != 1:                                              #Loop to check if the user has enetered 1 or other than 1
        if user_number == 0 or user_number == 1:                         #input validation for 0 and 1 to stop infinite loops r closeing program unexpectedly
            print("you presssed either 0 or 1......closing",end='')
            sys.exit()
        else:                                                            #Getting the value and updates it
                user_number = collatz(user_number)
                print(user_number)
except ValueError:                                               #input validation
    print("please enter a valid numebr", end = '')

import time, sys
indent_space = 0 #This shows how many spaces to indent
#user_value = int(input("Please enter a natural number value to specify space indetation"))
#if user_value <= 0:
  #  print("please correct your value!")
  # Need more modification for strict value entry

increment_indent = True #This tells to increase the spaces

try:
    while True: #The main function with infinte loop which will be closed by user with ctrl+C
        print(' ' * indent_space, end='')
        print('*********')
        time.sleep(0.15) # Pause for 15 Microseconds To make the execution a little bit beatiful and detectable
        if increment_indent: # If inrement_indent is true this will run
            #Code to increase the indentation
            indent_space = indent_space + 1
            if indent_space == 10: #Change this value accordingly or uncomment te user_value
                #change direction
                increment_indent = False # This will break the if statement and we will go to else
        else:
            #To decrease the number of spaces
            indent_space = indent_space - 1
            if indent_space == 0:
            #Change direction again
                increment_indent = True # And the loop will start from the beginning
except KeyboardInterrupt: #Keyboardinterupt is the error name for whe Ctrl+C is passed
    print("Closing the program")
    sys.exit()


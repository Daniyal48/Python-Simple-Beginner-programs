"""
Q1:What are the two values of the boolean data type: How do you write them?
Ans:Two values are True and False. They are written in a way that the first letter of the True or False is capital
    and it is written without any qoutes then it will work other wise python can give us error

Q2: What are the three boolean operators?
Ans: Three boolean operators are: 1) "or" 2) "and" 3) "not"

Q3: Write the truth tables of each Boolean opeartor (that is. every possible combination of Boolean values for the operator and what they evaluate to)
Ans: AND:
    True and True ------------> True
    True and False -----------> False
    False and True ----------> False
    False and True ----------> False

Q4:What do the following expression evaluate to?
Ans:(5 > 4) and (3 == 5)--------------------------> False
    not (5 > 4) ----------------------------------> False
    (5 > 4) or (3 == 5) --------------------------> True
    not ((5 > 4) or (3 == 5)) --------------------> Flase
    (True and True) and (True == False) ----------> False
    (not False) or (not True) --------------------> True

Q5:What are the six comparison opeartors?
ANs:Six comparison operators are:
    1: < (Less than)
    2: > (Greater than)
    3: <= (Less than or equal to)
    4: >= (Greater than or equal to)
    5: == (Equal to)
    6: != (Not Equal)

Q6: What is the difference between Equal to and assignment operator?
Ans:The equal to (==) opeartor compares two values whether they are equal or not and we can use it in if statement to make decisions
    while assignment operator (=) assigns a value to a variable, in other words it makes something Equal to a certain value.
    for examle if we say a = 5 it means that whenever we use a in our program it wil mean that we are talking about the value 5 not a exactly so becasue
    of = operator a becomes equal to 5.

Q7: Explain what a condition is and where will you use one?
Ans: A condition is a statement, by the results of which we can make certain decisions if a condition is true we can perform a certain task
and if a condition is false we can ignore that task and do something else or even do nothing.
Google Answer: Conditions are statements that are caused by the programmer which evaluates actions in the program and evaluates if it's true or false
               My point: we use it in the programs where we are unspecific of somethng and have more than one possibility

Q8:identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
Ans: The program has three blocks:
    Block 1: starts from line 51 an ends on line 52
    Block 2: starts from line 40 and ends on line 50
    Block 3: Line 47 to 53

Q9: Write a code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam and prints Greetings! if anything else is stored?
Ans: we can have multiple approaches but the best idea I have is the following:
    spam = str(input())
    if spam == '1':
        print ('Hello')
    elif spam == '2':
        print('Howdy')
    else:
        print("Greetings")

Q10:What keys can you press when a program is stuck in inifinte loop?
Ans: WE can use CTRL+C keys to shut the program

Q11:What is the difference between break and continue?
Ans: Breaks completely breaks the loop while continue only skips the current iteration and start a new one. In both the Break and Continue statements 
    the code after these statements will not be executed.

Q12: What is the diffrence between range(10) , range (0,10) and range(0,10,1)
Ans: In range (10) python will use the defaut values for start and step that are 0 and 1 respectively if we set stop (that is 10 right now) as 0 or a negative number 
    this functionwill not work in that case.
    In range(0,10), python will use default value for step that is 1 but this function also return an empty sequence if we set the stop value (10) less than start value that is (0)
    For range (0,10,1) everythng will work because we are completely modifying the value, only in one condition python will throw an error if we set the stop value to zero
Q13: Write a short program that prints numbers from 1 to 10 using for loop and then an equivalent program using while loop
Ans: FOR LOOP:
for i in range (1,11,1):
    print (i)
WHILE LOOP:
i = 1
while i < 11:
    print (i)
    i = i+1

Q14: If you had a  function named bacon() inside a module named spam, how would you call it after importing spam.
Ans: I would use the ModuleName.Function() to call it in this case spam.Bacon() and it will work.

Extra credit: Look up the round() and abs functions on the internet and find out waht they do. Experiment with them in the interactive shell
Ans: abs() Function: This is a built-in python function which returns an absolute value of a number that is passed to it. In simple words,
    It returns a positive number no matter what umber is passed to it. It is helpful in calculating scalers quantity.
    round() Function:
    This Function rounds off a decimal number to the decimal places specified. the syntax is 
    round(decimal_number,Number_of_decimal_Places)
    PROGRAMS FOR abs:

while True:
    print("Please enter a negative number to test abs() ")
    User_in = int(input())
    if User_in < 0:
        print("The absolute number is " + str(abs(User_in)))
    else:
        continue

PROGRAM FOR ROUND NUMBER:"""
while True:
    print("Please enter a number to round it off")
    User_in = float(input())
    print("Please enter a value for least decimal points")
    User_point = int(input())
    print("The rounded vaue is " + str(round(User_in,User_point)))

If my answers are incorrect or I have not explained properly you can comment or simpy ccontacct me I will be happy to know and correct my mistake. Also you should send me your own explaination and I will include it to the file.




Q1:Why are functions advantageous to have in your program?
Ans: Functions are important in our program because they are used to avoid code duplication. When we have to perform a certain task in our program multiple times we don't have to write the code for it again and again this makes the program debugging and updating difficult. In function, we define the function in our program just once and whenever we have to perform that function or task we simply call that functions which makes programming easier.

Q2:When does the code in function execute: When the function is defined or when the function is called?
Ans:The code in the function is executed when the function is called not when the function is defined.

Q3:What statement creates a function?
Ans: The def statement followed by command name and parenthesis with its own block creates a function. Syntax for function creation is,
def function_name(arguments):
    function_code_here

Q4:What is the difference between a function and a function call?
Ans: Function means the actual code used to perform the action and the function call means that to use that function whenever needed. The function in jus the code it isn't executed without the function call and when we use function call we are actually executing the function code.

Q5:How many global scopes are there in Python program? How many local scopes?
Ans:There is only one global scope in python which is created in the main body of a python program. Local scopes depends on the number of function we have in ur program because a local scope is generated in a function and doesn't exist outside that function.

Q6:What happens to variables in a local scope when the function call returns?
Ans:The local scope variables are terminated and removed their memory is freed by the Python interpreter and they are regenerated on the next function call.

Q7:What is a return value? Can a return be part of an expression?
Ans:A return value is the result which is returned by a function when it performs an action and the next step in the program depends on it. Yes a return can be a part of expression.

Q8:If a function does not have a return statement, what is the return value of a call to that function?
Ans: The return value will be null value.

Q9:How can you force a variable in a function to refer to the global variable?
Ans:By using the "global" keyword we can force the variable.

Q10:what is the data type of None?
Ans:None itself is a data type; yes the data type will be "None".

Q11:What does the import areallyyourpetsnamederic statement do?
Ans:This statement will import a mdule named "areallyyourpetsnamederic" which I think is a custom module and the file should exist in the same directory where the program importing is located therwise Python will not be able to read this file we wouldn't be able to use the functions inside this module.

Q12:If you had a function named bacon() in a module named spam, how would you call it after importing spam?
Ans:We can use this function by using the name of the module followed by the dot "." and then the function name we are using, here the syntax will be:
spam.bacon()

Q13:How can you prevent a program from crashing when it gets an error?
Ans:We will use the programing technique called "Exception Handling" by using try except statements which performs a task until an error is caught. we can direct the error either to null or stop the program execution. it totally depends on the developer how he use it and also the program requirement.

Q14:What does into the try clause? what goes into the except clause?
Ans:Try cause executes the code normally but when it gets something they can cause error or something then except clause is executed where we put an exception for a certain input or task. for example, we will use try clause where normal division will hapen but as soon as we divide a number by zero the except clause will execute where we will have defined the error already for the zero division.

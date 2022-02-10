# Author: Daniyal Shahzad
#Dated: 10/02/2022
## Further Updates will include sisgned and unsigned conversion
## Binary addition and subtraction
## Binary float Point addtion and subtraction
## Binary multiplication
## Complements 2's and 1's Complements
## Support and same features for other numbers system too.

def decimal_to_binary(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    else:
        return decimal_to_binary(num // 2) + str(num % 2)


# Main program
num = int(input('Enter a number: '))
print(decimal_to_binary(num))

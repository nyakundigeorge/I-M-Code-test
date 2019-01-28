# Author: George Nyakundi Nyaribo
# Date: 28/1/2019
# Python version used: python 3.6.7
# # Question 1: a.	Write a function is Prime that returns true if a number is prime.
# To Test/Run this function 
# 1. Modify the call to the function isPrime() by passing the value that you want to check.
# 2. Execute the command on the Terminal/CommandLine `python isPrime.py`

def isPrime(valueTocheck):
    # Value passed should be an Integer otherwise reject with a false
    #
    if type(valueTocheck) == int:
        if valueTocheck == 0 or valueTocheck == 1:
            return False
        elif valueTocheck == 2 or valueTocheck == 3:
            return True
        else:
            # For any integer in between 3 to the valueToCheck, if the modulus of the
            #  valuetoCheck and Integer is not equal to zero then that number is an Prime Number
            for item in range(3,valueTocheck):
                if(valueTocheck % item == 0):
                    return False
                return True
    else:
        return False
    



print(isPrime(61))
# Author: George Nyakundi Nyaribo
# Date: 28/1/2019
# Python version used: python 3.6.7
# # Question 1: a.	Write a function is Prime that returns true if a number is prime.
# To Test/Run this function
# 1. Modify the call to the function isPrime() by passing the value that you want to check.
# 2. Execute the command on the Terminal/CommandLine `python Main.py`


def isPrime(valueTocheck):
    """ 
    Function that Checks is a value is a prime number and return true if it is and false otherwise
    Argument: Integer
    Returns: Boolean
    """
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
            for item in range(3, valueTocheck):
                if(valueTocheck % item == 0):
                    return False
                return True
    else:
        return False


#  Question 1: b.) Write a function called memoize that takes any other function as input and returns a memoized version of that function
# 1. Takes the func as an argument and returns a function
# 2. Create a dictionary that'll hold the already evaluated/calculated values
# 3. Define a function func_child that takes value that has been passed on the iteration
# 4. Checks whether the entry with this val exists in teh local_copy, If not call the function to calculate it's value

def memoize(func):
    """
    A function that takes func as an argument and returns a function 
    Returns a memoized version of that function.
    """
    # this variable will act as a store of our already calculated values
    local_copy = {}

    def func_child(val):
        # check if the value passed is already existing in out local_copy, if yes, return the value from the dictionary if not calculate the value.
        if val not in local_copy:
            local_copy[val] = func(val)
        return local_copy[val]
    return func_child


#  Question 1: c.)Use the function in 3 above to memoize the is Prime function you wrote for problem 2

isPrimeMemoized = memoize(isPrime)


# Question 2. Write a function search  that accepts two arguments:
# a) A collection of values
# b) a value to find in the collection

# The function search should implement a binary search on the collection.
# If the value isn’t found in the collection, then the search function should return -1.
# If the value is found in the collection, then the function should return the first index of the value in the array.


# Assumptions:
# Our Collection will be ordered

# My first solution will be a recursive one since Binary Search involves splitting the collection into two halves
# and comparing the midvalue with the value to search, such that if the midvalue is less than the value to search
# we'll proceed to search the upper half otherwise we'll search the lower half till we find the position of the value we're looking for
# Conclusion: the recursive solution slices the initial collection hence making it hard for me to get the index of the value_to_find,
def recursive_search(collection, value_to_find):
    found = False
    # Check if the function has receieved a valid collection
    if len(collection) == 0:
        return -1
    # Check if the value to find is a valid integer
    # if type(value_to_find) != int:
    #     return -1

    middle_item = len(collection)//2

    # check if the middle item is equal to our value_to_find
    if collection[middle_item] == value_to_find:
        found = True
    else:
        if value_to_find > collection[middle_item]:
            return search(collection[middle_item + 1:], value_to_find)
        else:
            return search(collection[:middle_item], value_to_find)

    if found:
        return collection.index(value_to_find)
    else:
        return -1

# My Second and  solution will be a Iterative one since Binary Search involves splitting the collection into two halves
# and comparing the midvalue with the value to search, such that if the midvalue is less than the value to search
# Our main trick will be shifting the index_of_the first_item or index_of_the_last_item depending on whether the value in the midpoint
# is greater or less than the value_to_find
# Conclusion: the Interative solution was able to allow me find the index of the value_to_find if it existed in the collection since
# this solution doesn't invovle slicing the initial collection


def search(collection, value_to_find):
    # have a boolean variable the we'll use to check whether the value has been found or not
    found = False
    # Safety check to only allow us work with a collection of more than on element
    if len(collection) == 0:
        return -1
    # we'll use these variables dictate from what point our search begins or end
    index_of_first_item = 0
    index_of_last_item = len(collection)-1  # Lists in python are zero based

# our idea is to check that the index_of_the_first_item is always less than or equal to index_of_the_last_item.
# It's needful to mention that we're the found boolean variable is important since it'll help to stop the iteration.
# if the value_to_find is greater than the midpoint then we'll shift our index_of_first_item to the position middle_item + 1
# otherwise we'll shift the index_of_last_item to middle_item - 1
    while index_of_first_item <= index_of_last_item and not found:
        middle_item = (index_of_first_item + index_of_last_item)//2

        if collection[middle_item] == value_to_find:
            found = True
        else:
            if value_to_find > collection[middle_item]:
                index_of_first_item = middle_item + 1
            else:
                index_of_last_item = middle_item - 1

    if found:
        return collection.index(value_to_find)
    else:
        return -1


# print(PrimeMemoized(32))
# print(isPrimeMemoized(32))
print(search([0, 1, 2, 8, 13, 17, 19, 32, 42], 42))

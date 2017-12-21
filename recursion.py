##practical 7 recursion 

##A number, a, is a power of b if it is divisible by b and a/b is a power of b.
##Write a recursive function called is_power(a,b) that takes parameters a and b
##and returns True if a is a power of b, False otherwise. Could you write an
##iterative version of this function?

def is_power(a, b):
##2^2 = 4
##2^3 = 8 // a is 8, b is 2
    if b == 0:
        if a == 0:
            return True
    else:
        return False   ##2/0 = undefined
    if a == 1:
        return True ##case of b^0, B != 0
    elif a == b:
        return True ##cases for b^1
    if a % b == 0:
        return is_power(a/b, b)
    else:
        return False







##Write a recursive function rec_sum(numbers) that take a list of integers as a
##parameter and returns the sum of all the elements in the list. The function
##should return 0 if the list is empty.

def rec_sum(numbers):
##    if numbers == []:
##        return 0
##    else:
##        return numbers[0] + rec_sum(numbers[1:])

########### without using recursion #############
    if numbers == []:
        return 0
    total = 0
    for i in numbers:
        total = total + i
    return total




##Write a recursive function sum_all(numbers) that takes a multidimensional
##list of integers as parameters and returns the sum of all elements in that
##list. Note, empty lists sum to 0.


def sum_all(numbers):
    if numbers == []:
        return 0
    elif isinstance(numbers, list):
        return sum_all(numbers[0]) + sum_all(numbers[1:])
    elif isinstance(numbers, (float, int)):
        return numbers
    else:
        raise TypeError

##try with ([1, 2, [3, 4]])

##Write a recursive function flatten(mlist) where mlist is a multidimensional
##list that returns all the element from mlist into a one-dimensional list.
##Note, empty lists are ignored.


def flatten(mlist):
    if mlist == []:
        return []
    elif isinstance(mlist, list):
        return flatten(mlist[0]) + flatten(mlist[1:])
    elif isinstance(mlist, (float, int)):
        return [mlist]
    else:
        raise TypeError
    
##check if it is a list, if it is a list, return numbers
##check if it is a number, if it is a number, append list
















    

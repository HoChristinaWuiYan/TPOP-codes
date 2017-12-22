def is_power(a, b):   
    if a == 0 and b == 0:
        return True
    elif a == 0:
        raise ValueError
    if a!= 0:
        c = a/b
    elif a%b == 0 and c%b == 0:
        return True
    else:
        return False


def rec_sum(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + rec_sum(numbers[1:])
    
def sum_all(numbers):
    if numbers == []:
        return 0
    elif isinstance(numbers, list):
        return sum_all(number[0]) + sum_all(numbers[1:])
    elif isinstance(numbers, (float, int)):
        return numbers
    else:
        raise TypeError


        

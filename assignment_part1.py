def list_divide(numbers, divide=2):
    counter = 0
    for num in numbers:
        if num % divide == 0:
            counter += 1
    return counter

class ListDivideException(Exception):
    pass

def test_list_divide():
    if list_divide([1,2,3,4,5]) != 2:
        raise ListDivideException
    if list_divide([2,4,6,8,10]) != 5:
        raise ListDivideException
    if list_divide([30,54,63,98,100], divide=10) != 2:
        raise ListDivideException
    if list_divide([]) != 0:
        raise ListDivideException
    if list_divide([1,2,3,4,5], 1) != 5:
        raise ListDivideException

test_list_divide()
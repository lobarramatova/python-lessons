PI = 3.14
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    
    return  max_number

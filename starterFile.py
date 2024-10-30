#Your code goes here. 

import math

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def process_list(input_list):
    total = 0
    for item in input_list:
        try:
            number = int(item) 
            total += number ** 2
        except(TypeError , ValueError):
            continue
    return total
            

def nested_operations(a, b):
    try: 
        a = int(a)
        b = int(b)
        try: 
            answer = a / b 
            try:
                return math.sqrt(answer)
            except ValueError: 
                return "No real root exist for the values entered."
        except ValueError: 
                return "Indivisible values entered."
    except ValueError:
        return "Invalid values entered."


def process_input(a):
    try:
        a = input(a)
        answer = float(a)
        result = answer ** 2
    except ValueError:
        print("Unable to generate square of this input.")
        return None
    else:
        return result
    finally:
        print('Processing complete')


def main():
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(process_list([1, 2, 3, 4, 5]))    
    print(nested_operations(16, 4))
    print(nested_operations(10, 0))
    print(nested_operations(4, 5))
    process_input() 

    
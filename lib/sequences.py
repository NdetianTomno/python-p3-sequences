#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0, 1]  

    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(fibonacci)
    else:
        while len(fibonacci) < length:
            next_number = fibonacci[-1] + fibonacci[-2]  
            fibonacci.append(next_number)  
        print(fibonacci)


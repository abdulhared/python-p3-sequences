#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    if length >= 1:
        sequence.append(0)
    if length >= 2:
        sequence.append(1)
    
    for i in range(2, length):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    print(sequence)
    pass
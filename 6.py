
# Q6. (Sets + Tuples + Modules)
# Write a program that:
# Takes 10 numbers as input and stores unique numbers in a set.
# Converts that set into a tuple.
# Uses random module to pick and print 3 random numbers from the tuple.
# Uses math module to print the square root of the sum of the tuple elements.
# Handle possible exceptions.

import random
import math

numbers = set()

try:
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        numbers.add(num)

    t = tuple(numbers)

    print("Set:", numbers)
    print("Tuple:", t)

    print("3 Random Numbers:", random.sample(t, 3))

    total = sum(t)
    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Please enter numbers only!")

except Exception :
    print("Error:")


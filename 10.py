# Q10. (Mini Project - Comprehensive)
# Create a Smart Calculator & Data Manager program that combines multiple
# concepts:
# Use a while loop menu with these options:
# 1. Basic Arithmetic (use functions + exception handling)
# 2. Scientific Calculations (use math module)
# 3. Generate Random Numbers (use random module)
# 4. Store Results in Dictionary (with timestamp using string)
# 5. View History (show stored results)
# 6. Exit



import math
import random

history = {}

while True:
    print("\n1. Arithmetic")
    print("2. Scientific")
    print("3. Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            op = input("Enter operator (+,-,*,/): ")

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b

            print("Result =", result)

        except:
            print("Invalid Input")

    elif ch == 2:
        n = int(input("Enter number: "))
        result = math.sqrt(n)
        print("Square Root =", result)

    elif ch == 3:
        result = random.randint(1, 100)
        print("Random Number =", result)

    elif ch == 4:
        time = input("Enter timestamp: ")
        history[time] = result
        print("Result Stored")

    elif ch == 5:
        print("History")
        for i in history:
            print(i, ":", history[i])

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
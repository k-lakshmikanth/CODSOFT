######################################################################
# CALCULATOR
# TASK 2
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result
######################################################################

import os
clear = lambda: os.system('cls')

def retry(func):
    def inner():
        while True:
            try:
                return func()
            except ValueError:
                print("!! Invalid input. Please try again. !!\n")
    return inner

@retry
def add():
    print("\nAddition")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 + num2

@retry
def sub():
    print("\nSubtraction")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 - num2

@retry
def mul():
    print("\nMultiplication")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 * num2

@retry
def div():
    print("\nDivision")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1 / num2

def menu():
    global choice
    print("""
Operations:
0. Menu
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Clear
6. Exit
""")

@retry
def set_choice():
    global choice
    choice = int(input("Enter your choice: "))

functions = [menu, add, sub, mul, div, clear]
choice = 0

while choice != 6:
    if choice in (0, 5):
        functions[choice]()
    else:
        print(f"Result: {functions[choice]()}\n")
    set_choice()
print("\nExiting...\n")
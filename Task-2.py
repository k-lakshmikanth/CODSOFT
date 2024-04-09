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

@retry
def set_choice():
    global choice
    choice = int(input("Enter your choice: "))

def menu():
    global choice
    clear()
    print("""
Operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
""")
    set_choice()


functions = [add, sub, mul, div]
choice = 0

menu()
while choice in range(1, 5):
    print(f"Result: {functions[choice-1]()}\n")
    input("Press Enter to continue...")
    menu()
print("\nExiting...\n")
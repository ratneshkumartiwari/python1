import math

def addition(num1, num2):
    return float(num1) + float(num2)
def substraction(num1, num2):
    return float(num1) - float(num2)
def multiplication(num1, num2):
    return float(num1) * float(num2)
def division(num1, num2):
    return float(num1) / float(num2)
def square(num1):
    return float(num1) * float(num1)
def power(num1, num2):
    return float(num1)**float(num2)

print("type 1 for addition")
print("type 2 for substraction")
print("type 3 for multiplication")
print("type 4 for division")
print("type 5 for square")
print("type 6 for power")
opt = input("type the option: ")

if opt == "1":
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    print(addition(num1, num2))

if opt == "2":
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    print(substraction(num1, num2))

if opt == "3":
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    print(multiplication(num1, num2))

if opt == "4":
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    print(division(num1, num2))

if opt == "5":
    num1 = input("type first number: ")
    print(square(num1))

if opt == "6":
    num1 = input("type first number: ")
    num2 = input("type second number: ")
    print(power(num1, num2))
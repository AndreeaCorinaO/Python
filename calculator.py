# 5 operations add, substraction, multiply, division, modulo

#data input required two numbers floats and an operators


def add(num1,num2):
    result = num1 + num2 
    return result 

def substract(num1,num2):
    result = num1 - num2 
    return result 

def multiply(num1, num2):
    result = num1 * num2 
    return result 

def divide(num1, num2):
    result = num1 / num2 
    return result 

def modulo(num1, num2):
    result = num1 % num2 
    return result 

def user_input():
    
    number1 = float(input("Please enter and number: "))
    number2 = float(input("Please enter a second number: "))

    operator = input("Please enter the operator that you want [ +, -, /, %, *]: ")
    return number1, number2, operator

try:        
    number1, number2, operator = user_input()


    if operator == '+':
        result = add(number1, number2)
        print(result)
    elif operator == '-':
        result = substract(number1, number2)
        print(result)
    elif operator == '*':
        result = multiply(number1 , number2)
        print(result)
    elif operator == '%':
        result = modulo(number1 , number2)
        print(result)
    elif operator == '/':
        result = divide(number1 , number2)
        print(result)
    else:
        print("Operator not supported!")

except ValueError as ve:
        print("Something bad happened ")
        print(ve)
except TypeError as te:
        print("Something bad happened ")
        print(te)
except ZeroDivisionError as ze:
        print("Something bad happened ")
        print(ze)
except Exception as ee:
        print("Something really bad happeneed")
        print(ee)
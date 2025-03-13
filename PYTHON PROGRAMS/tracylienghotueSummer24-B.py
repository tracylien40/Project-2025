#  LCCSSummer24-B 
# Name: Tracy
# This function multiplies two numbers 
def multiply(x, y):
    return x * y 
# This function divides two numbers
def divide(x, y):
    return round (x / y,1)
def add(x,y):
    return x + y
def subtract (x,y):
    return x - y
# Main Program
import random # To generate random numbers
print("Select operation.")
print("1.Multiply")
print("2.Divide")
print("3.Add")
print("4.Subtract")
# Take input from the user 
choice = input("Enter choice(1/2/3/4/):")
num1=float(input("Enter first number"))
num2=float(input("Enter second number"))           


if choice == '1':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '2':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '3':
    print(num1, "+",num2,"=", add(num1,num2))
elif choice == '4':
    print(num1, "-",num2,"=",subtract(num1,num2))




#  LCCSSummer24-A 
# Name: Tracy Lienghotue
#This calculator can only add and subtract
num1 = 9
num2 = 5
name=input("Please enter your name")
print("Hello", name)
print("Welcome to the addition and subtraction calculator")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

print('Do you want me to (a)dd or (s)ubtract?')
choice = input()


if choice == 'a' or choice == 'A':
    print (num1 + num2 , "=",)
    

elif choice == 's' or  choice =='S':
    print (num1 - num2 , "=")
    


elif choice == 'w':
    print("inavlid  option")



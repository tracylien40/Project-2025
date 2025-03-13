# Name: Tracy Lienghotue
#This calculator can only add and subtract

num1 = 9
num2 = 5
name=input("Enter your name")
print("Hello",name )
num1=int(input("Enter first number"))
num2=int(input("Enter a second number"))
print('Do you want me to (a)dd or (s)ubtract?')
choice = input()


if choice == 'a'or  choice=='A':
    print (num1 + num2)
    
elif choice == 's' and choice=='S':
    print (num1 - num2)
    
elif choice =='w': 
    print("Invalid Option")



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Prompt the user to enter a choice (a for addition, s for subtraction, w to exit)
choice = input("Enter 'a' for addition, 's' for subtraction, or 'w' to exit: ")

# Check the user's choice and perform the corresponding operation
if choice.lower() == 'a':
    print(num1 + num2)  # Addition
elif choice.lower() == 's':
    print(num1 - num2)  # Subtraction
elif choice.lower() == 'w':
    print("Invalid Option")  # Display message for 'w' (exit option)
else:
    print("Invalid Option")  # Display message for any other invalid input
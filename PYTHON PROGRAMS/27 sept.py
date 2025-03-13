# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate simple interest

# Ask the user for the principal
principal =float(input("Enter principal: "))


# Ask the user for the interest rate
rate = float(input("Enter rate: "))

# Ask the user for the length of time
time = float(input("Enter time in years: "))


# Simple interest calculation
amount = principal * rate * time

# Display the answer
print("The interest amount is", amount)
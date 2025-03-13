# A program to find the mode of a list of values
# Version 1

# Initialise a list of ages
L = [18, 16, 17, 18, 19, 18, 17]

# Build up a list of unique values
unique_values = []
for value in L:
    if value not in unique_values:
        unique_values.append(value)

# Build up a list of frequencies
frequencies = []
for value in unique_values:
    frequency = L.count(value)
    frequencies.append(frequency)

# Find the mode
max_frequency = max(frequencies)
max_frequency_pos = frequencies.index(max_frequency)
mode = unique_values[max_frequency_pos]

print("Mode is", mode)
print("Max_Freq", max_frequency)
print("Max_Freq_Pos", max_frequency_pos)


# EXPERIMENT ...
# Ask students how they know the program is working? (i.e. actual result vs. expected result)
# Change the values in the list and see what happens?
# Change the variable names as see what happens
# What happens if there was a) no mode b) several modes
# Does this program work for a list of strings (e.g. ["Mary", "Andy", "Pat"])? Why/why not?

# TASKS FOR BREAKOUT
# Save this program as mode2.py
# Change the comment at the top of the program to say Version 2
# Modify the code so that it displays the frequency of the mode
# The statement list(set(L)) returns a list of unique elements in L. Use this information to shorten the code
# The program works if the list has a single mode. Modify the code so that it ....
# - works if there is no mode e.g. L = [18, 16, 17, 21, 19, 16, 22]
# - works if there are multiple modes e.g. L = [18, 16, 17, 18, 17, 18, 17]
# Discuss how the code could be made more modular
# Test each little change as you go
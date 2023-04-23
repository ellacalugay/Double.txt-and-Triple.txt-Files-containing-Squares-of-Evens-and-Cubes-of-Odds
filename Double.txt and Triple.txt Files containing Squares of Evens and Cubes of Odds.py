# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #4 | PROBLEM 4
# Creating a program that will create to separate files containing the squares of all even and cubes of all odds.

def computation():
# Pseudocode
# Open the file named integers.txt for reading, double.txt for appending, and tripple.txt for appending.
    with open ("integers.txt", "r") as integers, open("double.txt", "a") as squared, open("tripple.txt", "a") as cube:
    # Read each line in integers.txt.
        # If the integer is even, square it. 
            # Append the squared value of even integers to double.txt
        # If the integer is odd, cube it.
            # Append the cube value of odd integers to tripple.txt
# End of the code.
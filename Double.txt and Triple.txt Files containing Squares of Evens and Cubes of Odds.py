# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #4 | PROBLEM 4
# Creating a program that will create to separate files containing the squares of all even and cubes of all odds.

# Pseudocode
import tkinter as tk

def computation(): # defining a function
    # Create a tkinter window
    root = tk.Tk()
    root.title("PROBLEM 4")

    # Create a frame for the output
    frame = tk.Frame(root, bd=2, relief="groove")
    frame.pack(padx=10, pady=10)
    
# Open the file named integers.txt for reading, double.txt for appending, and tripple.txt for appending.
    with open ("integers.txt", "r") as integers, open("double.txt", "a") as squared, open("tripple.txt", "a") as cube:
        # Read each line in integers.txt.
        for line in integers:
            input_number = int(line)
            # If the integer is even, square it. 
            if input_number % 2 == 0:
                square_even = input_number * input_number
                # Append the squared value of even integers to double.txt
                squared.write (str(square_even) + "\n")
            # If the integer is odd, cube it.
            else:
                cube_odd = input_number * input_number * input_number
                # Append the cube value of odd integers to tripple.txt
                cube.write (str(cube_odd) + "\n")

computation() # calling a function
# End of the code.
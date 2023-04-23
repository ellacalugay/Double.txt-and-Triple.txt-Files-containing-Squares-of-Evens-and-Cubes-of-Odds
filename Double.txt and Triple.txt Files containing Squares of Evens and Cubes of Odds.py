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

    # Create labels for the output files with border and border color
    double_label = tk.Label(frame, text="Squares", font=("Arial", 12, "bold"), bg="yellow", bd=2, relief="groove")
    double_label.grid(row=0, column=0, padx=10)

    triple_label = tk.Label(frame, text="Cubes", font=("Arial", 12, "bold"), bg="red", bd=2, relief="groove")
    triple_label.grid(row=0, column=1, padx=10)

    # Add a border to the top of the output
    top_border = tk.Frame(frame, bg="blue", height=2, width=200)
    top_border.grid(row=1, columnspan=2, pady=(10,0))

    # Open the file named integers.txt for reading
    with open("integers.txt", "r") as integers:
        row = 3
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
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
    with open ("integers.txt", "r") as integers, open("double.txt", "a") as squared, open("tripple.txt", "a") as cube:        
        row = 3
        # Read each line in integers.txt.
        squares = []
        cubes = []
        for line in integers:
            input_number = int(line)
            # If the integer is even, square it.
            if input_number % 2 == 0:
                squared_even = input_number ** 2
                squared.write(str(squared_even) + "\n")
            # If the integer is odd, cube it.
            else: 
                cube_odd = input_number ** 3
                cube.write(str(cube_odd) + "\n")

        # Define the functions
        def load_squares():
            clear_output()
            with open("double.txt", "r") as squared_file:
                squares = squared_file.readlines()
                for idx, square in enumerate(squares):
                    square_label = tk.Label(frame, text=square, bg="magenta")
                    square_label.grid(row=idx+3, column=0)

        def load_cubes():
            clear_output()
            with open("tripple.txt", "r") as cube_file:
                cubes = cube_file.readlines()
                for idx, cube in enumerate(cubes):
                    cube_label = tk.Label(frame, text=cube, bg="magenta")
                    cube_label.grid(row=idx+3, column=1)

        def load_output():
            if mode.get() == "Squares":
                load_squares()
            else:
                load_cubes()

        def load_close():
            for bye in frame.winfo_children():
                if bye != top_border and bye != double_label and bye != triple_label:
                    bye.destroy()
            root.destroy()  # Terminate the program by closing the main window

        def clear_output():
            for child in frame.winfo_children():
                if child != top_border and child != double_label and child != triple_label:
                    child.destroy()

        # Create buttons for switching between squares and cubes output
        mode = tk.StringVar()
        mode.set("Squares")
        square_button = tk.Radiobutton(root, text="Even", variable=mode, value="Squares", bg="yellow")
        square_button.pack(side="left", padx=(0,10))

        cube_button = tk.Radiobutton(root, text="Odd", variable=mode, value="Cubes", bg="red")
        cube_button.pack(side="left", padx=(0,10))

        load_button = tk.Button(root, text="Load Output", command=load_output, bg="green")
        load_button.pack(side="left")

        close_button = tk.Button(root, text="Close", command=lambda: [clear_output(), load_close()], bg="blue")
        close_button.pack(side="left")

    # Start the tkinter event loop
    root.mainloop()

# Call the computation function 
computation() 

# End of the code.
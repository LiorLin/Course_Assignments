import tkinter as tk

# Define unit multipliers
concentration_units = {"M": 1, "mM": 1e-3, "uM": 1e-6, "nM": 1e-9}
volume_units = {"L": 1, "mL": 1e-3, "uL": 1e-6, "nL": 1e-9}

# Define the calculation logic
def calculate():

    try:
        # Collect input values and stores it to a variable : 
        c1 = entry1.get()
        v1 = entry2.get()
        c2 = entry3.get()
        v2 = entry4.get()
        
        # Collect the scroll down unit input 
        # and use it approach the numeric value from the relevant dictionary : 
        c1_multiplier = concentration_units[var1.get()]
        v1_multiplier = volume_units[var2.get()]
        c2_multiplier = concentration_units[var3.get()]
        v2_multiplier = volume_units[var4.get()]

        # Convert provided values to floats with their units (if a value was provided)
        # Else stores a "None" value. 
        values = [
            float(c1) * c1_multiplier if c1 else None,
            float(v1) * v1_multiplier if v1 else None,
            float(c2) * c2_multiplier if c2 else None,
            float(v2) * v2_multiplier if v2 else None,
        ]

        # Ensure exactly one value is missing
        if values.count(None) != 1:
            result_label.config(text="Please provide exactly 3 inputs.")
            return

        # Identify the missing value and calculate it based on the formula C1*V1 = C2*V2

        if values[0] is None:  # C1 is missing
            values[0] = values[2] * values[3] / values[1]
            result = values[0] / c1_multiplier

            # Update the value in the entery field : 
            entry1.delete(0, tk.END) # Clear text in enetery field
            entry1.insert(0, f"{result:.6g}") # Insert the formatted result in the entry field. 

        elif values[1] is None:  # V1 is missing
            values[1] = values[2] * values[3] / values[0]
            result = values[1] / v1_multiplier
            entry2.delete(0, tk.END)
            entry2.insert(0, f"{result:.6g}")

        elif values[2] is None:  # C2 is missing
            values[2] = values[0] * values[1] / values[3]
            result = values[2] / c2_multiplier
            entry3.delete(0, tk.END)
            entry3.insert(0, f"{result:.6g}")

        elif values[3] is None:  # V2 is missing
            values[3] = values[0] * values[1] / values[2]
            result = values[3] / v2_multiplier
            entry4.delete(0, tk.END)
            entry4.insert(0, f"{result:.6g}")

        # Update the result label
        result_label.config(text="Calculation complete.")

        # if the the inputs are non numeric or invalid : 
    except ValueError: 
        result_label.config(text="Invalid input. Please enter numeric values.")

# Creating the main application window :

root = tk.Tk() # Initialize the main application window
root.title("Volume-Concentration Calculator")

# Adding the title label and location in the window : 
title_label = tk.Label(root, text="Volume-Concentration Calculator", font=("Arial", 14))
title_label.grid(row=0, column=0, columnspan=6, pady=10)

# Define options and input containers :
entries = []  # Store references to input fields
dropdown_vars = []  # Store StringVars for dropdowns

# Dropdown menu options :
concentration_options = ["M", "mM", "uM", "nM"]
volume_options = ["L", "mL", "uL", "nL"]

# Row 1 - C1 and C2 :

# C1
label1 = tk.Label(root, text="C1:", anchor="w")
label1.grid(row=1, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, width=15)
entry1.grid(row=1, column=1, padx=5, pady=5)
entries.append(entry1)
var1 = tk.StringVar(value=concentration_options[0])
dropdown1 = tk.OptionMenu(root, var1, *concentration_options)
dropdown1.grid(row=1, column=2, padx=5, pady=5)
dropdown_vars.append(var1)

# C2
label3 = tk.Label(root, text="C2:", anchor="w")
label3.grid(row=1, column=3, padx=5, pady=5)
entry3 = tk.Entry(root, width=15)
entry3.grid(row=1, column=4, padx=5, pady=5)
entries.append(entry3)
var3 = tk.StringVar(value=concentration_options[0])
dropdown3 = tk.OptionMenu(root, var3, *concentration_options)
dropdown3.grid(row=1, column=5, padx=5, pady=5)
dropdown_vars.append(var3)

# Row 2 - V1 and V2 :

# V1
label2 = tk.Label(root, text="V1:", anchor="w")
label2.grid(row=2, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, width=15)
entry2.grid(row=2, column=1, padx=5, pady=5)
entries.append(entry2)
var2 = tk.StringVar(value=volume_options[0])
dropdown2 = tk.OptionMenu(root, var2, *volume_options)
dropdown2.grid(row=2, column=2, padx=5, pady=5)
dropdown_vars.append(var2)

# V2
label4 = tk.Label(root, text="V2:", anchor="w")
label4.grid(row=2, column=3, padx=5, pady=5)
entry4 = tk.Entry(root, width=15)
entry4.grid(row=2, column=4, padx=5, pady=5)
entries.append(entry4)
var4 = tk.StringVar(value=volume_options[0])
dropdown4 = tk.OptionMenu(root, var4, *volume_options)
dropdown4.grid(row=2, column=5, padx=5, pady=5)
dropdown_vars.append(var4)

# Adding the Calculate Button : 
calculate_button = tk.Button(root, text="Calculate", command=calculate)
 # Associates the button with the executation of the calculate function. 
calculate_button.grid(row=3, column=0, columnspan=6, pady=10)

# Adding the Result Label :
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=6, pady=5)

print("c")# Starting the main loop
root.mainloop()

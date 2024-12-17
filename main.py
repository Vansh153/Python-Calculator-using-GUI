import tkinter as tk                   # import the tkinter module because tkinter is a libary and tk is use the alias of the module 
from tkinter import messagebox         # means that import the messagebox module using the tkinter module 

# Functions for calculator operations
def add(a, b):                    # create a function name  is and add pass the two arguments in a and b
    return a + b                  # return the value a plus b e.g(a+b)

def subtract(a, b):               # create a function name is substract and pass the two arguments in a and b
    return a - b                  # return the value a minus b e.g(a-b)

def multiply(a, b):               # create a function name is multiply and pass the two argument in a and b
    return a * b                  #  return the value a multiply b e.g(a*b)

def divide(a, b):                                  # create a function name is divide and pass the two arguments in a and b
    if b == 0:                                     # if is a condition statement,if b == 0: means b equals to 0 
        return "Error! Division by zero."          # then return the value is "Error ! Divisional by zero"
    return a / b                                   # otherwise a is divided by b

# Function to handle the calculation                     
def calculate():                                   #  create a function name is calculator ()
    try:                                           # try and except blocks  are used to handle excepation that may occur execution of program.
        num1 = float(entry1.get())                 # num1 is a variable and float() is a  floating point number . entry1.get() is tk.Entry in Enterted by the user.
        num2 = float(entry2.get())                 # num2 is a varibale and float() is a floating number numberand .entry.get() is tk.entry in enterted by the user.
        operation = operation_var.get()            # operation_var is a tkitner string variable and .get stored in operation. 

        
        if operation == "+":                       # if is a conditional statement operation equals to plus  e.g(operation == "+")
            result = add(num1, num2)                    # then result is a variable equals to add the two number is (num1 and num2)

        elif operation == "-":                     # elif is a conditional statement operation equals to minus e.g(operation == "-")
            result = subtract(num1, num2)               # then result is a variable equals to subtract the two number is (num1 and num 2)

        elif operation == "*":                     # elif is a conditional statement operation equals to multiply e.g(operation == "*")
            result = multiply(num1, num2)                # then result equals to multiply the two number is (num1 and num2)

        elif operation == "/":                     # elif is a condition statement operation equals to divided e.g(operation == "/")
            result = divide(num1, num2)                    # then result is a variable equals to divided by the two numbers is (num1 and num2)

        else:                                        # else is a condition statement
            result = "Invalid operation!"            # result is equal to the invalid operation

        result_label.config(text=f"Result: {result}")    #result_label is display the GUI and config is the update the configuration of resul label                     
    except ValueError:                                             # except ValueError means the  raise the value  error            
        messagebox.showerror("Input Error", "Please enter valid numbers!")   # messagebox is a tkinter of the module and show error() is a shows a error
                                                                             # input error is a dialog box and please enter a shows the error.

# Create the main window
root = tk.Tk()                              # root is a varible to store tk is tkinter module and TK() create a window application using GUI.      
root.title("simple calculator")             # root.title() is used to tkinter module to store  title of the window of GUI
 
# Create input fields and labels
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)  # create a label using tkinter module and # root is the main application of tkiner and display the text.
entry1 = tk.Entry(root)                                                           # entry 1 is a variable and tk is single line text using gui entred the input value 
entry1.grid(row=0,column=1,padx=10,pady=10)                                      # entry is size of grid box row and column using grid method.

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10) #create a label using the tkinter module # root is the main application of tkiner and display the text.
entry2 = tk.Entry(root)                                                   # entry2 is a variable and tk is single line text using gui enterted the input value
entry2.grid(row=1, column=1, padx=10, pady=10)                            # entry 2 is size of the grid box row and column uisng grid method.

# Dropdown menu for operation selection
tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)    # create a label using the tkinter module  # root is the main application of tkiner gui and display the text of 
operation_var = tk.StringVar(value="+")                                             # create a operational_var to store the tk module and manage the string values in gui application 
                                                                                    # value is a paramter value '+' additional operation

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")   # create a variable name operational menu and tk is a module using the dropdown menu of gui and operation_var is a string the values and then are many options like "+,-,*,/"
operation_menu.grid(row=2, column=1, padx=10, pady=10)                    #  operation menu is a dropdown menu using the tkinter module in a  grid box using row and columns etc.    

# Button to perform calculation
calc_button = tk.Button(root, text="Calculate", command=calculate)       # create a button variable name is calc_button using the tkinter module in gui application.the button is created by calculator clicked the function call
calc_button.grid(row=3, column=0, columnspan=2, pady=10)                #The calculator button to store the tk module in a gridlayout specify   the using row and columnn etc.


# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))     # create a variable name is result label and tk.lable is a module of  creating the label using the GUI and root is the main application of gui text the results and then font size 
result_label.grid(row=4, column=0, columnspan=2, pady=10)              # result label is the tkinter module e.(tk.label) in grid layout then specify the row and colum and columspna

# Run the GUI application
root.mainloop()   
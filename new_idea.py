import aiofiles
import tkinter as tk



# Press CTRL + H, then in the "Find" box, type "var1".  In the "Replace" box, type the username or identifier you want to use and press replace all instances.  Repeat this with the remaining var(x)
var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
var6 = 0
var7 = 0
var8 = 0
var9 = 0
var10 = 0

total_azoth = int(var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10)

#with open("account1.txt", "r") as file:
   



'''
later use

lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]

'''

def gui():
    
    # Account 1
    
    global var1
    
    # Create root window and add title
    r = tk.Tk()
    r.title('Azoth Manager')
    
    # Create label with total azoth amount
    total_azoth_amount = tk.Label(r, text = "Total Azoth:(WIP)")

    # Build label
    total_azoth_amount.place(relx=0.0, rely=1.0, anchor="se") # DONT WORK

    # Add text with the username of the first account
    account_1 = tk.Label(r, text="var1:")
    
    # Create a label of total azoth that updates with var1
    account_1_total = tk.Label(r, text=var1)
    
    # Create a button to add 999 to the value of var1 everytime it is clicked
    account_1_add_stack = tk.Button(r, text = 'Add 999', width = 10, command = add_999_to_var1)
    
    # Create a button to remove 999 to the value of var1 everytime it is clicked
    account_1_remove_stack = tk.Button(r, text = 'Remove 999', width = 10, command = remove_999_to_var1)
    
    # Build buttons/labels
    account_1.grid(sticky = "w", row = 1, column = 1)
    account_1_total.grid(sticky = "w", row = 1, column = 2)
    account_1_add_stack.grid(sticky = "w", row = 1, column = 3)
    account_1_remove_stack.grid(sticky = "w", row = 1, column = 4)

    # Account 2

    global var2
    
    # Add text with the username of the second account
    account_2 = tk.Label(r, text="var2:")
    
    # Create a label of total azoth that updates with var2
    account_2_total = tk.Label(r, text=var2)
    
    # Create a button to add 999 to the value of var2 everytime it is clicked
    account_2_add_stack = tk.Button(r, text = 'Add 999', width = 10, command = add_999_to_var2)
    
    # Create a button to remove 999 to the value of var2 everytime it is clicked
    account_2_remove_stack = tk.Button(r, text = 'Remove 999', width = 10, command = remove_999_to_var2)
    
    # Build buttons/labels
    account_2.grid(sticky = "w", row = 2, column = 1)
    account_2_total.grid(sticky = "w", row = 2, column = 2)
    account_2_add_stack.grid(sticky = "w", row = 2, column = 3)
    account_2_remove_stack.grid(sticky = "w", row = 2, column = 4)
    
    # Account 3

    global var3
    
    # Add text with the username of the second account
    account_3 = tk.Label(r, text="var3:")
    
    # Create a label of total azoth that updates with var3
    account_3_total = tk.Label(r, text=var3)
    
    # Create a button to add 999 to the value of var3 everytime it is clicked
    account_3_add_stack = tk.Button(r, text = 'Add 999', width = 10, command = add_999_to_var3)
    
    # Create a button to remove 999 to the value of var3 everytime it is clicked
    account_3_remove_stack = tk.Button(r, text = 'Remove 999', width = 10, command = remove_999_to_var3)
    
    # Build buttons/labels
    account_3.grid(sticky = "w", row = 3, column = 1)
    account_3_total.grid(sticky = "w", row = 3, column = 2)
    account_3_add_stack.grid(sticky = "w", row = 3, column = 3)
    account_3_remove_stack.grid(sticky = "w", row = 3, column = 4)
    
    r.mainloop()
    


def remove_999_to_var1():
    global var1
    var1 = var1 - int(999)
    print("Removed a stack from var1.")
    print("Total:", var1)

def add_999_to_var1():
    global var1
    var1 = var1 + int(999)
    print("Added a stack to var1.")
    print("Total:", var1)
    
def remove_999_to_var2():
    global var2
    var2 = var2 - int(999)
    print("Removed a stack from var2.")
    print("Total:", var2)

def add_999_to_var2():
    global var2
    var2 = var2 + int(999)
    print("Added a stack to var2.")
    print("Total:", var2)
    
def remove_999_to_var3():
    global var3
    var3 = var3 - int(999)
    print("Removed a stack from var3.")
    print("Total:", var3)

def add_999_to_var3():
    global var3
    var3 = var3 + int(999)
    print("Added a stack to var3.")
    print("Total:", var3)
    
def calculate_total_azoth():
    global total_azoth
    

gui()
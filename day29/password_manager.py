# Importing required libraries
import tkinter  # For creating GUI
import string  # For accessing ASCII letters, digits, and punctuation
import json  # For handling JSON data storage
import random  # For generating random passwords
from tkinter import messagebox  # For displaying dialog boxes

# Creating main window
windows = tkinter.Tk()  # Initialize the main application window
windows.title("Password Manager")  # Set window title
windows.config(padx=20, pady=20)  # Add padding around window edges

# Setting up the logo
canvas = tkinter.Canvas(width=200, height=200)  # Create canvas for logo
lock_image = tkinter.PhotoImage(file="logo.png")  # Load logo image
canvas.create_image(100, 100, image=lock_image)  # Place logo in canvas center
canvas.grid(column=1, row=0)  # Position logo in grid

# Website input section
website_label = tkinter.Label(text="Website", font=("courier", 15, "bold"))  # Create website label
website_label.grid(column=0, row=1)  # Position website label

web_entry = tkinter.Entry(width=50)  # Create website entry field
web_entry.grid(column=1, row=1, columnspan=2)  # Position entry field across 2 columns

# Email input section
email_label = tkinter.Label(text="Email/Username", font=("courier", 15, "bold"))  # Create email label
email_label.grid(column=0, row=2)  # Position email label

email_entry = tkinter.Entry(width=50)  # Create email entry field
email_entry.grid(column=1, row=2, columnspan=2)  # Position entry field across 2 columns

# Password input section
password_label = tkinter.Label(text="password", font=("courier", 15, "bold"))  # Create password label
password_label.grid(column=0, row=3)  # Position password label

password_entry = tkinter.Entry(width=32)  # Create password entry field
password_entry.grid(column=1, row=3)  # Position password entry field

def generate_password():
    # Initialize list to store character selections
    selected_charaters_list = []
    punc_list = list(string.punctuation)  # Get list of punctuation characters
    letters_list = list(string.ascii_letters)  # Get list of ASCII letters
    digit_list = list(string.digits)  # Get list of digits
    total_lists = [punc_list, letters_list, digit_list]  # Combine all character types
    
    # Select random characters from each character type
    for lists in total_lists:
        selected_charaters_list.append(random.sample(lists, k=random.randint(6,8)))
    
    # Flatten the list and shuffle
    password_list = [i for row in selected_charaters_list for i in row]
    random.shuffle(password_list)
    
    # Join characters into password string
    password = ''.join(password_list)
    password_entry.insert(tkinter.END, string=password)  # Insert password into entry field

# Create generate password button
gen_password = tkinter.Button(text="Generate Password", width=14, highlightthickness=0, command=generate_password)
gen_password.grid(column=2, row=3)

# Initialize storage for passwords
storage = list()

def reading_details():
    """Read previously saved passwords from JSON file"""
    global storage
    try:
        with open('C:/Users/awaki/Desktop/100.py/day29/saved_password.json', encoding="utf-8") as f:
            storage = json.load(f)
    except FileNotFoundError:
        print("sorry we could not locate file saved_score.json, we are now creating it")

reading_details()  # Load saved passwords when program starts

def saving_details():
    """Save new password details to storage"""
    # Add new entry to storage list
    storage.append({"website": web_entry.get(), "email": email_entry.get(), "password": password_entry.get()})
    
    try:
        # Verify fields are not empty
        if len(web_entry.get()) > 0 and len(password_entry.get()) > 0:
            # Show confirmation dialog
            validate = messagebox.askokcancel(title=f"{web_entry.get()}", 
                                            message=f'Here are you details\n Email : {email_entry.get()},\n Password : {password_entry.get()}')

            if validate == True:
                # Save to JSON file if user confirms
                with open('C:/Users/awaki/Desktop/100.py/day29/saved_password.json','w',encoding='utf-8') as f:
                    json.dump(storage, f, ensure_ascii=False, indent=4)

                # Clear entry fields after saving
                web_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
        else:
            messagebox.showwarning(title="oops", message="please make sure to fill in the fields")

    except FileNotFoundError:
        messagebox.showerror(title="FileNotFoundError", message="sorry we couldn't locate the file saved_score.json")

# Create save button
store_password = tkinter.Button(text="Add", width=42, command=saving_details)
store_password.grid(column=1, row=4, columnspan=2)

# Start the application main loop
windows.mainloop()

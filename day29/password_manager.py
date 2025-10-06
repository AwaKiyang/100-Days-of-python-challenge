# Import required libraries
import tkinter  # Used to create the graphical user interface (GUI)
import string  # Provides access to ASCII letters, digits, and punctuation
import json  # Enables reading and writing data in JSON format
import random  # Used to generate random passwords
from tkinter import messagebox  # Used to display pop-up dialog boxes

"""
=========================================================================================
                         MAIN INTERFACE OF THE PASSWORD MANAGER
=========================================================================================
"""

# ---------------------Create the main window-------------------_---------#
windows = tkinter.Tk()  # Initialize the main window
windows.title("Password Manager")  # Set the title of the application window
windows.config(padx=20, pady=20)  # Add padding to the window edges for better spacing

# --------------------------------Set up the logo section--------------------------#
canvas = tkinter.Canvas(width=200, height=200)  # Create a canvas for the logo image
lock_image = tkinter.PhotoImage(file="logo.png")  # Load the logo image
canvas.create_image(100, 100, image=lock_image)  # Display the logo at the center of the canvas
canvas.grid(column=1, row=0)  # Position the logo in the grid layout

# ---------------------------------Website input field--------------------------------#
website_label = tkinter.Label(text="Website", font=("courier", 15, "bold"))  # Label for website input
website_label.grid(column=0, row=1)  # Position the label on the grid

web_entry = tkinter.Entry(width=32)  # Entry field where user types the website
web_entry.grid(column=1, row=1)  # Position the entry field next to the label

# -------------------------------Email/Username input field------------------------------#
email_label = tkinter.Label(text="Email/Username", font=("courier", 15, "bold"))  # Label for email input
email_label.grid(column=0, row=2)  # Position the label on the grid

email_entry = tkinter.Entry(width=50)  # Entry field for user’s email or username
email_entry.grid(column=1, row=2, columnspan=2)  # Span across two columns for more space

# -------------------------------------Password input field-----------------------------#
password_label = tkinter.Label(text="password", font=("courier", 15, "bold"))  # Label for password input
password_label.grid(column=0, row=3)  # Position the label on the grid

password_entry = tkinter.Entry(width=32)  # Entry field for generated or custom password
password_entry.grid(column=1, row=3)  # Position the entry field next to the label

"""
=========================================================================================
                            PASSWORD GENERATION FUNCTION
=========================================================================================
"""

def generate_password():
    """
    ######################## FUNCTION TO GENERATE A RANDOM PASSWORD ########################
    Generates a random password using letters, digits, and punctuation.
    The result is displayed automatically in the password input field.
    """
    # -----------------------Initialize an empty list to store randomly selected characters------------------#
    selected_charaters_list = []
    punc_list = list(string.punctuation)  # List of all punctuation marks
    letters_list = list(string.ascii_letters)  # List of lowercase and uppercase letters
    digit_list = list(string.digits)  # List of numeric characters
    total_lists = [punc_list, letters_list, digit_list]  # Combine all character types
    
    # ------------------------Randomly pick between 6 and 8 characters from each list-----------------------------#
    for lists in total_lists:
        selected_charaters_list.append(random.sample(lists, k=random.randint(6,8)))
    
    # --------------------------Flatten nested lists and shuffle the order-------------------------------------#
    password_list = [i for row in selected_charaters_list for i in row]
    random.shuffle(password_list)
    
    # ------------------------------Join all characters to form the final password-------------------------------#
    password = ''.join(password_list)
    password_entry.insert(tkinter.END, string=password)  # Display password in the entry field

# -----------------------Button to generate a random password--------------------------------#
gen_password = tkinter.Button(text="Generate Password", width=14, highlightthickness=0, command=generate_password)
gen_password.grid(column=2, row=3)


"""
=========================================================================================
                           READ EXISTING PASSWORDS FUNCTION
=========================================================================================
"""
# -------------------------Initialize password storage list---------------------------------#
storage = list()

def reading_details():
    """
    ######################## FUNCTION TO READ SAVED PASSWORDS ########################
    Reads previously saved password entries from a JSON file and loads them into memory.
    """
    global storage
    try:
        with open('C:/Users/awaki/Desktop/100.py/day29/saved_password.json', encoding="utf-8") as f:
            storage = json.load(f)  # Load existing data from JSON file
    except FileNotFoundError:
        print("File not found: saved_password.json. A new one will be created upon saving.")

reading_details()  # Load existing saved passwords at startup

"""
=========================================================================================
                            SAVE NEW PASSWORD FUNCTION
=========================================================================================
"""

def saving_details():
    """
    ######################## FUNCTION TO SAVE PASSWORD DETAILS ########################
    Saves the current website, email, and password fields into a JSON file.
    Displays a confirmation box before saving.
    """
    # Add a new record to the storage list
    storage.append({"website": web_entry.get(), "email": email_entry.get(), "password": password_entry.get()})
    
    try:
        # Check that both website and password fields are not empty
        if len(web_entry.get()) > 0 and len(password_entry.get()) > 0:
            # Ask user for confirmation before saving
            validate = messagebox.askokcancel(title=f"{web_entry.get()}", 
                                            message=f'Here are your details\n Email : {email_entry.get()},\n Password : {password_entry.get()}')

            if validate == True:
                # Save the updated data to the JSON file
                with open('C:/Users/awaki/Desktop/100.py/day29/saved_password.json','w',encoding='utf-8') as f:
                    json.dump(storage, f, ensure_ascii=False, indent=4)

                # Clear the input fields after saving
                web_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
        else:
            # Show warning if any field is empty
            messagebox.showwarning(title="Oops", message="Please make sure to fill in all fields")

    except FileNotFoundError:
        # Handle missing JSON file error
        messagebox.showerror(title="FileNotFoundError", message="Could not locate saved_password.json file")

# Button to save entered password details
store_password = tkinter.Button(text="Add", width=42, command=saving_details)
store_password.grid(column=1, row=4, columnspan=2)

"""
=========================================================================================
                           SEARCH STORED CREDENTIAL FUNCTION
=========================================================================================
"""
def search_info():
    """
    ######################## FUNCTION TO SEARCH FOR SAVED WEBSITE INFO ########################
    Searches the stored credentials for the entered website name and displays
    the corresponding email and password if found.
    """
    websites_list = [website_info['website'] for website_info in storage]  # Extract list of stored websites
    
    if web_entry.get() in websites_list:
        for website_info in storage:
            if website_info["website"] == web_entry.get():
                messagebox.showinfo(title=f'{website_info['website']}', message=f'Here are your details\n EMAIL : {website_info["email"]},\n PASSWORD : {website_info['password']}')
    else:
        # Notify user if website is not found in storage
        messagebox.showinfo(title="Result", message="Website not found")
            

# Button to trigger website search
search = tkinter.Button(text="Search", width=14, command=search_info)
search.grid(column=2, row=1)

# Run the main Tkinter event loop
windows.mainloop()

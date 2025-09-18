import tkinter  # Import the tkinter library for GUI

window = tkinter.Tk()  # Create the main window
window.title("MY first Gui program")  # Set window title
window.minsize(width=500, height=500)  # Set minimum window size

my_label = tkinter.Label(text="I AM a Label", font=("Arail", 24, "bold"))  # Create a label widget
my_label.pack()  # Add the label to the window

my_label["text"] = "New text"  # Change the label text

def button_clicked():
    print("button click")  # Print message when button is clicked

button = tkinter.Button(text="click me", command=button_clicked)  # Create a button widget
button.pack()  # Add the button to the window

# entry
user_input = tkinter.Entry()  # Create an entry widget for user input
user_input.pack()  # Add the entry to the window
user_input.get()  # Get the current text from the entry (not used here)

window.mainloop()  # Start the GUI event loop
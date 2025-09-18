import tkinter  # Import the tkinter library for GUI

windows = tkinter.Tk()  # Create the main window
windows.title("My second GUI Program")  # Set window title
windows.minsize(width=500, height=500)  # Set minimum window size

my_label = tkinter.Label(text="Waar", font=("Arail", 24, "bold"))  # Create a label widget
my_label.pack()  # Add the label to the window

entry = tkinter.Entry()  # Create an entry widget for user input
entry.pack()  # Add the entry to the window

def change_label():
    my_label["text"] = entry.get()  # Update label text with entry content

button = tkinter.Button(text="click me", command=change_label)  # Create a button that calls change_label
button.pack()  # Add the button to the window

windows.mainloop()  # Start the GUI event loop
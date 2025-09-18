import tkinter
window = tkinter.Tk()
window.title("Mile to kM Converter")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

entry = tkinter.Entry()
entry.grid(column=2, row=1)

miles_label = tkinter.Label(text="MILES")
miles_label.grid(column=3, row=1)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=1, row=2)

value = tkinter.Label(text="0")
value.grid(column=2,row=2)

km_label = tkinter.Label(text="KM")
km_label.grid(column=3, row=2)

def convertion():
    value["text"] =float(entry.get()) * 1.609
button = tkinter.Button(text="Calculate", command=convertion)
button.grid(column=2, row=3)




window.mainloop()

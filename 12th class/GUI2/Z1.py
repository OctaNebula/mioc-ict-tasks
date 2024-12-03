import tkinter as tk


def change_text():
    label.config(text="red")

def windowColor():
    root.configure(background='red')

def buttonthing():
    change_text()
    windowColor()

root = tk.Tk()
root.title("Z1")

button = tk.Button(root, text="Click me!", command=buttonthing)
button.grid(row=2, column=0)

#image of python logo above the button
logo = tk.PhotoImage(file="python.png")
label = tk.Label(root, image=logo)
label.grid(row=1, column=0)

label = tk.Label(root, text="Hello, Tkinter!")
label.grid(row=0, column=0)

root.mainloop()


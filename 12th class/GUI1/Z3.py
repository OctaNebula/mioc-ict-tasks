import tkinter as tk

root = tk.Tk()

root.geometry("400x400")
root.title("Z3.py")

def cmd():
    print("Hello World")

button = tk.Button(root, text="Click Me", command=cmd)
button.pack()

root.mainloop()
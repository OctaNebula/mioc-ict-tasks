import tkinter as tk

root = tk.Tk()

geometry = input()
root.geometry(geometry)
root.title("Z2.py")
a = tk.Label(root, text="Hello World")
a.pack()

root.mainloop()
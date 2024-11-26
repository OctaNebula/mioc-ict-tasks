import re
import tkinter as tk

root = tk.Tk()
root.title("Z5.py")
root.geometry("50x53")

topframe = tk.Frame(root)
topframe.pack()

gumbA = tk.Button(root, text="Gumb A", fg="blue")
gumbA.place(relx=0, rely=0, anchor=tk.NW)
gumbB = tk.Button(root, text="Gumb B", fg="green")   
gumbB.place(relx=1, rely=0, anchor=tk.NE)
gumbC = tk.Button(root, text="Gumb C", fg="red")
gumbC.place(relx=0.5, rely=1, anchor=tk.S)

root.mainloop()
from os import write
import tkinter as tk

root = tk.Tk()
root.title("Z4")

def writeToText():
    with open("text.txt", "w") as f:
        f.write(text.get("1.0", tk.END))

text = tk.Text(root, width=30, height=10)
text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
btn = tk.Button(root, text="Create txt", command=writeToText)

root.mainloop()

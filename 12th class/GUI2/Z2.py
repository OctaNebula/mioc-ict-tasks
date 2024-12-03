import tkinter as tk

root = tk.Tk()
root.title("Z2")

btn = tk.Button(root, text="Click me")
btn.place(relx=0.5, rely=0.9, anchor="s", relwidth=1.0)

img = tk.PhotoImage(file="python.png")
lbl = tk.Label(root, image=img)
lbl.place(relx=0.5, rely=0.5, anchor="center", relheight=0.5, relwidth=0.5)

txtlabel = tk.Label(root, text="Hello, world!")
txtlabel.place(relx=0.5, rely=0.1, anchor="n")

root.mainloop()

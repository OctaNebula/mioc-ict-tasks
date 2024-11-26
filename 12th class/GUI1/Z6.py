import tkinter as tk

root = tk.Tk()
root.title("Z6.py")

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))

label1 = tk.Label(root, text="First Number:")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Second Number:")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Add", command=add)
button.grid(row=2, column=1)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()
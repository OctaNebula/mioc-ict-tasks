import tkinter as tk
root = tk.Tk()
root.title("Z4.py")
root.geometry("260x100")

name = tk.Label(root, text="Name and Surname: ").grid(row=0, column=0, padx=5, pady=5)
id = tk.Label(root, text="ID: ").grid(row=1, column=0, padx=5, pady=5)


nameSurnameInput = tk.Entry(root).grid(row=0, column=1)
idInput = tk.Entry(root).grid(row=1, column=1)

#nameSurnameInput.pack(padx=5, pady=5)
#idInput.pack(padx=5, pady=5)

def submit(): # adds the name and surname to ucenici.txt alongside with the ID
    with open("ucenici.txt", "a") as f:
        f.write(f"{nameSurnameInput.get()} - {idInput.get()}")
    
submitButton = tk.Button(root, text="Submit", command=submit)
submitButton.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
import tkinter as tk

name = ""
subject = ""
error = False

def harvestName():
    global name
    name = studentName.get()
    studentName.delete(0, tk.END)

def harvestSubject():
    global subject
    global error
    subject = subjectName.get()
    subjectName.delete(0, tk.END)
    if subject == "":
        error = True
    else:
        error = False

def push():
    global error
    harvestName()
    harvestSubject()
    if error:
        textlbl.config(text=f"{name} nije upisao predmet")
    else:
        textlbl.config(text=f"Student {name} je upisao predmet {subject}")

root = tk.Tk()
root.geometry("400x400")

studentName = tk.Entry(root)
studentName.pack()

subjectName = tk.Entry(root)
subjectName.pack()


btn = tk.Button(root, text="Unesi", command=push)
btn.pack()

textlbl = tk.Label(root, text="Unesite tekst")
textlbl.pack()


root.mainloop()
import tkinter as tk

root = tk.Tk()

knowsEnglish = 0
knowsGerman = 0
knowsFrench = 0

label = tk.Label(root, text="Which languages do you know?")
label.pack()

# checkboxes
english = tk.Checkbutton(root, text="English", variable=knowsEnglish)
english.pack()

german = tk.Checkbutton(root, text="German", variable=knowsGerman)
german.pack()

french = tk.Checkbutton(root, text="French", variable=knowsFrench)
french.pack()

submit = tk.Button(root, text="Submit")
submit.pack()
def submit_action():
    global knowsEnglish, knowsGerman, knowsFrench
    if english_var.get():
        knowsEnglish += 1
    if german_var.get():
        knowsGerman += 1
    if french_var.get():
        knowsFrench += 1
    print(f"English: {knowsEnglish}, German: {knowsGerman}, French: {knowsFrench}")

english_var = tk.IntVar()
german_var = tk.IntVar()
french_var = tk.IntVar()

english.config(variable=english_var)
german.config(variable=german_var)
french.config(variable=french_var)

submit.config(command=submit_action)

printresbutn = tk.Button(root, text="Print result", command=lambda: print(f"English: {knowsEnglish}, German: {knowsGerman}, French: {knowsFrench}"))
printresbutn.pack()


root.mainloop()

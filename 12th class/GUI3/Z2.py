import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

def showGroupDropdown():
    groupDropdown.pack()
    groupButn.pack()
    groupTxt.pack()

def choose():
    chosen = dropdown.cget("text")
    displayChosen.config(text="Chosen: " + chosen)
    showGroupDropdown()

def choose2():
    chosen = groupDropdown.cget("text")
    groupTxt.config(text="Chosen: " + chosen)

dropdown = tk.OptionMenu(root, tk.StringVar(), 
                         "Linearna algebra",
                         "Matematička analiza",
                            "Programiranje",
                            "Fizika",
                            "Statistika",
                         )
dropdown.pack()

chooseButton = tk.Button(root, text="Choose", command=choose)
chooseButton.pack()

displayChosen = tk.Label(root, text="Chosen: ")
displayChosen.pack()

groupDropdown = tk.OptionMenu(root, tk.StringVar(),
                              "Jutarnja",
                                "Popodnevna",
)
groupButn = tk.Button(root, text="Choose group", command=choose2)

groupTxt = tk.Label(root, text="Group: ")

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

cheekybypass = 0
def choose():
    global cheekybypass
    chosen = dropdown.cget("text")
    current_text = displayChosen.cget("text")
    if cheekybypass == 0:
        cheekybypass = 1
        new_text = current_text + " " + chosen
    else:
        new_text = current_text + ", " + chosen
    displayChosen.config(text=new_text)

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

root.mainloop()
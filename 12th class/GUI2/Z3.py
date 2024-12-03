import tkinter as tk
root = tk.Tk()
root.title("Z4.py")
root.geometry("260x100")

def calculateAvgGrade():
    with open("ucenici.txt", "r") as f:
        grades = []
        for line in f:
            grades.append(int(line.split(" - ")[1]))
        avg = sum(grades) / len(grades)
        avgGrade.config(text=f"Average grade: {avg}")
        print(avg)


name = tk.Label(root, text="Name and Surname: ").grid(row=0, column=0, padx=5, pady=5)
grade = tk.Label(root, text="grade: ").grid(row=1, column=0, padx=5, pady=5)


nameSurnameInput = tk.Entry(root).grid(row=0, column=1)
idInput = tk.Entry(root).grid(row=1, column=1)

def submit(): # adds the name and surname to ucenici.txt alongside with the grade
    with open("ucenici.txt", "a") as f:
        f.write(f"{nameSurnameInput.get()} - {idInput.get()}")
    
submitButton = tk.Button(root, text="Submit", command=submit)
submitButton.grid(row=2, column=1, padx=5, pady=5)

calculateAvgGrade = tk.Button(root, text="Calculate average grade", command=calculateAvgGrade)
calculateAvgGrade.grid(row=3, column=1, padx=5, pady=5)

avgGrade = tk.Label(root, text="Average grade: ")
avgGrade.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()
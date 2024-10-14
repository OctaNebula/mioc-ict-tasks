class Student():
    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    def __repr__(self):
        return f'{self.name} {self.surname}, {self.birthdate}'

class SchoolClass(): # class that contains multiple Student() objects
    def __init__(self, students):
        self.students = students

    def admit(self, student):
        self.students.append(student)

    def bdToDays(self, bd): #converts birthdate to days
        bd = bd.split(".")
        return int(bd[0]) + int(bd[1]) * 30 + int(bd[2]) * 365

    def parameterSort(self, parameter):
        if parameter == "n":
            self.students.sort(key=lambda x: x.name)
        elif parameter == "s":
            self.students.sort(key=lambda x: x.surname)
        elif parameter == "b":
            self.students.sort(key=lambda x: self.bdToDays(x.birthdate))

    def __repr__(self): #prints all students in the class alphabetically via string
        return f"{', '.join([str(student) for student in self.students])}"

# test example

students = [Student("John", "Doe", "01.01.2000"), Student("Jane", "Doe", "01.01.2001"), Student("Alice", "Smith", "01.01.1999")]
schoolClass = SchoolClass(students)
print(schoolClass)
schoolClass.parameterSort("n")
print(schoolClass)
schoolClass.parameterSort("s")
print(schoolClass)
schoolClass.parameterSort("b")
print(schoolClass)
schoolClass.admit(Student("Bob", "Smith", "01.01.2002"))
print(schoolClass)

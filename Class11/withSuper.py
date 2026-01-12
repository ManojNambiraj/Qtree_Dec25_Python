class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name: ", self.name)

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        super().display()
        print("Roll no: ", self.roll_no)

s1 = Student("Kavi", 101)

s1.display()

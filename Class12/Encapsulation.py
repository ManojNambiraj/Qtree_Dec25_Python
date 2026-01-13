# Access specifiers:

    # Public
    # Private

# Encapsulation: (Getter & Setter)

class Student:
    def __init__(self, name, marks, DoB):
        self.name = name
        self.__marks = marks
        self.__DoB = DoB

    def setMarks(self, m1):
        self.__marks = m1

    def getMarks(self):
        return self.__marks
    
    def setDoB(self, date):
        self.__DoB = date

s1 = Student("Ravi", 0)

s1.setMarks(97)

print(s1.getMarks())
print(s1.name)
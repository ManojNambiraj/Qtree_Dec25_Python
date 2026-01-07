# OOPs --> Object Oriented Programmings

    # Class --> template
    # Object --> Real world Entity
    # Encasulation
    # Inheritance
    # Polymorp

class Car:
    no_of_wheels=0
    color=""
    no_of_sheets=0
    fuel_type=""
    speeds=0

    def speed(self):
        print("Speed of Car: ", self.speeds)

honda = Car()

honda.no_of_wheels = 5
honda.color = "red"
honda.no_of_sheets = 7
honda.fuel_type = "Petrol"
honda.speeds = 150

print(honda.color)

honda.speed()
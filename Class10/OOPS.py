# OOPS

class Car:
    def __init__(self, obj, wheels, color, sheets, fuel, sp):
        print("constructor Called")
        self.obj = obj
        self.no_of_wheels = wheels
        self.colors = color
        self.no_of_sheets = sheets
        self.fuel_type = fuel
        self.speed = sp

    def __str__(self):
        return self.obj

    def speeds(self):
        print(self)

    def __del__(self):
        print("Destructor Called")

honda = Car("honda", 4, "Blue", 6, "Petrol", 300)
toyoto = Car("toyoto", 4, "Blue", 6, "Petrol", 300)

print(honda.no_of_wheels)
print(honda.no_of_sheets)
print(honda.colors)

honda.speeds()

print(toyoto.no_of_wheels)
print(toyoto.no_of_sheets)
print(toyoto.colors)

toyoto.speeds()

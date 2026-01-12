# Inheritance

class Child:
    isHome = True

    def Behaviour(self):
        print("I'm Always Smiling")

class Parent:
    bankBalance = 500000

    # def Behaviour(self):
    #     print("I'm always Angry")

class GrantFather(Parent, Child):
    packetMoney = 100

    # def Behaviour(self):
    #     print("I'm always Joyfull")

student = GrantFather()

print(student.packetMoney)
print(student.bankBalance)
print(student.isHome)

student.Behaviour()
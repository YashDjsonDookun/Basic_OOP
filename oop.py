#!/usr/share/python3

class Vehicle:
    honkSound = "Basic Vehicle Horn"

    def __init__(self, make, model, color, year, mileage):
            self.make = make
            self.model = model
            self.color = color
            self.year = year
            self.mileage = mileage

    def Honk(self, honkSound):
        print(f"Honk: {honkSound}")

class Automobile(Vehicle):
    honkSound = "Pimp Pimp!!!"

    def __init__(self, make, model, color, year, mileage, numberOfWheels, typeOfAutomobile):
        # inherit attributes from Vehicle Superclass
        Vehicle.__init__(self, make, model, color, year, mileage)
        # Own attributes
        self.numberOfWheels = numberOfWheels
        self.typeOfAutomobile = typeOfAutomobile

    def DisplayAutomobileAttributes(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage}")
        print(f"Number Of Wheels: {self.numberOfWheels}")
        print(f"Type Of Automobile: {self.typeOfAutomobile}")

    def OpenDoors(self):
        print("Doors Opened!")

    def CloseDoors(self):
        print("Doors Closed!")

automobile = Automobile("Honda", "Fit", "Black", 2011, 69699, 4, "Car")
automobile.DisplayAutomobileAttributes()
automobile.Honk(Automobile.honkSound)
automobile.OpenDoors()
automobile.CloseDoors()

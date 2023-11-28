from random import randint

class Car():
    def __init__(self, regNum, maxSpeed, currSpeed = 0, traveledDstnc = 0):
        self.regNum        = regNum
        self.maxSpeed      = maxSpeed
        self.currSpeed     = currSpeed
        self.traveledDstnc = traveledDstnc

    def accelerate(self, change):
        self.currSpeed += change

        if self.currSpeed < 0:
            self.currSpeed = 0

        elif self.currSpeed >= self.maxSpeed:
            self.currSpeed = self.maxSpeed

    def drive(self, hours):
        self.traveledDstnc += int(hours * self.currSpeed)


class ElectricCar(Car):
    def __init__(self, regNum, maxSpeed, capacity):
        super().__init__(regNum, maxSpeed)
        self.capacity = capacity


class GasolineCar(Car):
    def __init__(self, regNum, maxSpeed, fuelTank):
        super().__init__(regNum, maxSpeed)
        self.fuelTank = fuelTank


gasCar    = GasolineCar("ACD-123", 165, 32.3)
electrCar = ElectricCar("ABC-15", 180, 52.5)

gasCar.accelerate(randint(0, 40))
electrCar.accelerate(randint(0, 40))

gasCar.drive(3)
electrCar.drive(3)

print(f"Gasoline Car's traveled distance: {gasCar.traveledDstnc}km\n"
      f"Electric Car's travled distance: {electrCar.traveledDstnc}km")
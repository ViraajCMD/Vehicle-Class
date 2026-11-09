class Vehicle:

    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240,234)

print(f"The maximum speed of model X is {modelX.max_speed}")

print(f"\nThe mileage for modelX is {modelX.mileage}")
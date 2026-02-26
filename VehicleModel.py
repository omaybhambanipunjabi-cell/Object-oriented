class Vechicle:
    def __init__(self, max_speed, mileage, colour):

        self.max_speed = colour

modelX = Vechicle(240, 18, "Yellow")
modelY = Vechicle(300, 20, "Blue")
Audi = Vechicle(285, 15, "Black")

print("Model 1 Colour: ", modelX.colour)
print("Model 1 Max speed: ", modelX.max_speed)
print("Model 1 Mileage: ", modelX.mileage)

print("\nModel 2 Colour: ", modelY.colour)
print("Model 2 Max Speed: ", modelY.max_speed)
print("Model 2 Mileage: ", modelY.mileage)

print("\nModel 3 Colour: ", Audi.colour)
print("Model 3 Max Speed: ", Audi.max_speed)
print("Model 3 Mileage: ", Audi.mileage)

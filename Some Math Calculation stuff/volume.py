OneOverThree = float(1/3)
PI = float(3.14)
Volume = float(input("Volume "))
Height = float(input("Height "))

Radius = OneOverThree * Volume / PI / Height

RadiusSquared = Radius**float(2)
print(OneOverThree * PI * RadiusSquared * Height)
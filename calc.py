print("Area of a cirlce:\n ")
print("Area of a rectangle:\n ")
print("Surface area of cylinder:\n ")

pi = 3.141

radius = float(input("Enter a radius:\n"))

print("\n--- Circle ---")
circle_area = pi * (radius ** 2)
print(f"The answer is {circle_area:.2f}")

print("\n--- Rectangle ---")
length = float(input("Enter the length: "))
width = float(input("Enter a width:\n"))

print("\n--- Cylinder ---")
area_of_rectangle = length * width
print(f"The answer is {area_of_rectangle:.2f}")

height = float(input("Enter a height:\n"))

surface_area = 2 * pi * radius * height + 2 * pi * (radius ** 2)
print(f"The surface area is {surface_area:.2f}")





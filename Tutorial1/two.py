from math import*

def areaperi(rad):
    area=pi*rad**2
    perimeter=2*pi*rad
    return f"area is: {area:.2f} & perimeter is: {perimeter:.2f}"

radius=int(input("Enter the radius of the circle: "))
calc=areaperi(radius)
print(calc)
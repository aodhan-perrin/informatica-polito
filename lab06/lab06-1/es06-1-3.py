from math import pi
from math import sqrt

def sphere_volume(r: int) -> float:
    return (4/3) * pi * r**3

def sphere_surface(r: int) -> float:
    return 4 * pi * r**2

def cylinder_volume(r: int, h: int) -> float:
    return h * pi * r**2

def cylinder_surface(r: int, h: int) -> float:
    return (2 * pi * r**2) + (2 * pi * r * h)

def cone_volume(r: int, h: int) -> float:
    return (1/3) * pi * h * r**2

def cone_surface(r: int, h: int) -> float:
    return pi * r * (sqrt(r**2 + h**2))


r = int(input("insert radius -> "))
h = int(input("insert height -> "))

print("shpere volume: ", round(sphere_volume(r), 2))
print("shpere surface: ", round(sphere_surface(r), 2))
print("cylinder volume: ", round(cylinder_volume(r, h), 2))
print("cylinder surface: ", round(cylinder_surface(r, h), 2))
print("cone volume: ", round(cone_volume(r, h), 2))
print("cone surface: ", round(cone_surface(r, h), 2))
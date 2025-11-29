# parameters
AIR_DRAG = 0.2  # air drag coefficient
RHO = 1.23      # air density (kg / m^3)
PROJ_A = 2.5    # vehicle projection area (m^2)


def drag(v: int) -> float:
    return 0.5 * RHO * (v**2) * PROJ_A * AIR_DRAG


def power(v: int) -> float:
    return drag(v) * v


def h_power(v: int) -> float:
    return power(v) / 745.7


v = float(input("insert velocity (m/s) -> "))

print(
    f"drag: {drag(v)}N\n"
    f"min power: {round(power(v), 2)}W\n"
    f"min horsepower: {round(h_power(v), 2)}Hp"
)

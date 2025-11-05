# circuit parameters
Vs = 40  # voltage (volts)
Rs = 8   # speaker impedence (ohms)
Ra = 20  # amp resistance (ohms)


def f_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def power(n: float) -> float:
    return Rs * (n*Vs / (Ra*n**2 + Rs))**2


n_ratios = []  # list of spiral ratios
ps = []        # list of power calculations

for n in f_range(0.01, 2, 0.01):
    n_ratios.append(round(n, 2))
    ps.append(power(n))

max_p = max(ps)

print(
    f"optimal n: {n_ratios[ps.index(max_p)]}\n"
    f"power output: {round(max_p, 2)}W"
)

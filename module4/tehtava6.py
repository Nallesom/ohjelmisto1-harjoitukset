import random
#N satunnaispisteiden kokonaismäärä
N = int(input())
#nn = ympyrän sisään osuvien pisteiden määrä
nn = 0

testatutpisteet = 0
while testatutpisteet != N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        nn += 1
    testatutpisteet += 1

piapprox = 4 * nn / N
print(f"Approximation of pi: {piapprox:.4f}")
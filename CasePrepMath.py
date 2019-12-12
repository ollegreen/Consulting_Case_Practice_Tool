# Row 7 = if the 2nd number is in thousands (t), millions(m) or billions(b).

import random

sys_random = random.SystemRandom()
multdiv = "*******/"
thousandsmillionsbillions = "kmb"

for _ in range(1000):
    value1 = sys_random.randint(0, 1000)
    value2 = sys_random.choice(multdiv)
    value3 = sys_random.randint(0, 1000)
    value4 = sys_random.choice(thousandsmillionsbillions)

mathnumbers = [value1, value2, value3, value4]

print(mathnumbers)

### генерация параметров эллиптическеой кривой
import random

q = 1021  # простое !!!
a = random.randint(2, q)
x = random.randint(2, q)
y = random.randint(2, q)
b = ((y ** 2) - ((x ** 3) + (a * x))) % q

while (4 * (a ** 3) + 27 * (b**2)) % q == 0:
    a = random.randint(2, q)
    x = random.randint(2, q)
    y = random.randint(2, q)
    b = ((y ** 2) - ((x ** 3) + (a * x))) % q

print(a, b, x, y)





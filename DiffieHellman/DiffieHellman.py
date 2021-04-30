import random
import sys

def public_key(k):

    return a ** k % n


def key_exchange(ka):
    ya = public_key(ka)
    kb = random.randint(2, n - 1)
    yb = public_key(kb)
    print('Открытый ключ собеседника:', yb)

    if yb ** ka % n == ya ** kb % n:
        print('Общий секретный ключ:', yb ** ka % n)
    else:
        print('Что-то пошло не так:', yb ** ka % n, ya ** kb % n)

    return yb ** ka % n


keys = list(map(int, input('Введите n, a и секретный ключ, меньшие n: ').split()))
n = keys[0]
a = keys[1]

if keys[1] > keys[0] or keys[2] > keys[0]:
    print('Значения секретного ключа и параметра а не должны превышать значение параметра n.')
    sys.exit(0)
elif public_key(keys[2]) == keys[2]:
    print('Открытый ключ равен секретному. Введите новые параметры.')
    sys.exit(0)
else:
    shared_private_key = key_exchange(keys[2] % n)
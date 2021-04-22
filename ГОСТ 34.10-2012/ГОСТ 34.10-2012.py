import math
import sys
import random
from sympy.ntheory import totient

def hash_(message, p):
    h = 0
    hash = 0
    for i in message:
        hash = (h + int(i) + 1) ** 2 % p
        h = hash

    return hash


def doubling_P(P, a, p):
    λ = ['', '']
    λ[0] = (3 * P[0] ** 2 + a) % p
    λ[1] = 2 * P[1] % p
    if λ[1] == 0:
        return 0
    if not (λ[0]/λ[1]).is_integer():
        λ[0] = λ[0] % p
        λ[1] = (λ[1] ** (totient(p) - 1)) % p
        λ = int(λ[0] * λ[1] % p)
    else:
        λ = int(λ[0]/λ[1])

    x = (λ ** 2 - 2 * P[0]) % p
    y = (λ * (P[0] - x) - P[1]) % p

    return x, y


def addition_P(P1, P2, p):
    λ = ['', '']
    λ[0] = (P2[1] - P1[1]) % p
    λ[1] = (P2[0] - P1[0]) % p
    if λ[1] == 0:
        return 0
    if not (λ[0]/λ[1]).is_integer():
        λ[0] = λ[0] % p
        λ[1] = (λ[1] ** (totient(p) - 1)) % p
        λ = int(λ[0] * λ[1] % p)
    else:
        λ = int(λ[0]/λ[1])

    x = (λ ** 2 - P1[0] - P2[0]) % p
    y = (λ * (P1[0] - x) - P1[1]) % p

    return x, y


def key_gen(P, k, a, p):
    k = bin(k)[3:]
    P_ = P
    for i in k:
        P_ = doubling_P(P_, a, p)

        if i == '1':
            P_ = addition_P(P, P_, p)

    return P_


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def quadratic_residues(p):
    quadrate = {}

    for i in range(p):
        quadrate[i] = (i ** 2 % p)

    return quadrate


def all_points(a, b, p, quadrate):
    y_quadrate = []

    for i in range(p):
        y_quadrate.append((i ** 3 + a * i + b) % p)

    points = []
    for i in range(p):
        for j in range(len(quadrate)):
            if y_quadrate[i] == quadrate[j]:
                points.append([i, j])

    return points


def find_q(amount_points):
    for i in range(amount_points+1, 1, -1):
        if amount_points % i == 0 and is_prime(i):
            return i


def generation_G(points, q, a, p):
    for i in points:
        if key_gen(i, q, a, p) == 0:
            return i


def check_curve(a, b, p):
    if not is_prime(p):
        print("Модуль кривой должен быть простым.")
        sys.exit(0)

    if (4 * (a ** 3) + 27 * (b ** 2)) % p == 0:
        print("Ваша кривая непригодна для вычислений, попробуйте ещё раз")
        sys.exit(0)

    return True


def generation_signature(message, xu, k):
    message_ = message_to_pos_unicode(message)
    hash = hash_(message_, q)

    if hash == 0:
        hash = 1

    yu = key_gen(G, xu, a, p)
    #print()
    #print('Генерация подписи')
    print('Открытый ключ Yu:', yu)
    #print('Значение хэша:', hash)
    P = key_gen(G, k, a, p)
    #print('Вычислим точку [k]G =', P)

    r = P[0] % q
    s = (k * hash + r * xu) % q
    print('Сообщение', message, 'подписано парой чисел:', (r, s))

    return message, r, s, yu


def signature_verification(message, r, s, yu):
    if r < 0 or r > q or s < 0 or s > q:
        print('Параметры s и r должны быть больше 0 и меньше', q)
        sys.exit(0)

    message_ = message_to_pos_unicode(message)
    hash = hash_(message_, q)
    if hash == 0:
        hash = 1

    #print('Значение хэша:', hash)

    u1 = s * hash ** (totient(q) - 1) % q
    #print('Найдем u1 =', u1)
    u2 = (-r * hash ** (totient(q) - 1)) % q
    #print('Найдем u2 =', u2)
    P1 = key_gen(G, u1, a, p)
    P2 = key_gen(yu, u2, a, p)
    P = addition_P(P1, P2, p)
    #print('Вычислим точку [u1]G + [u2]Yu =', P)
    #print('xp mod q =', P[0] % q, '= r =', r)
    if P[0] % q == r:
        print('Подпись верна.')
    else:
        print('Подпись не верна. xp mod q =', P[0] % q, 'и r =', r)


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))


#curves = [[2005, 7935, 8537, [7625, 3580], 127], [7270, 8322, 9137, [8189, 3901], 61], [5596, 1413, 9967, [2093, 4157], 229]]
#curve = random.choice(curves)


message = input('Введите сообщение: ')
curve = list(map(int, input('Введите параметры кривой через пробел, а также простой модуль: ').split()))

if check_curve(curve[0], curve[1], curve[2]):
    quadrate = quadratic_residues(curve[2])
    points = all_points(curve[0], curve[1], curve[2], quadrate)
    q = find_q(len(points) + 1)
    G = generation_G(points, q, curve[0], curve[2])

print('Введите закрытый ключ и рандомизатор, меньшие', q, ', через пробел: ')
key = list(map(int, input().split()))
a = curve[0]
b = curve[1]
p = curve[2]


"""
if key[0] > q or key[1] > q:
    print('Ключ и рандомизатор должны быть меньше', q)
    sys.exit(0)
"""

xu = key[0] % q
k = key[1] % q
print()
print('Кривая с параметрами a =', a, 'b =', b, 'p =', p)
print('Генератор точек =', G)

signature = generation_signature(message, xu, k)
print()
print('Проверка подписи')
message = input('Введите сообщение: ')
key = list(map(int, input('Введите значение подписи и открытый ключ через пробел: ').split()))
signature_verification(message, key[0], key[1], [key[2], key[3]])

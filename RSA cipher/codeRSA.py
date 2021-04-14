import math
import random
from textwrap import wrap
import sys
from sympy.ntheory import totient


def mutually_prime_number(a):   # ищем взаимно-простое число
    b = random.randint(2, 1000000)
    while math.gcd(a, b) != 1:
        b = random.randint(2, 1000000)

    return b


def solve_comparison(a, m):  # решаем сравнение

    return (a ** (totient(m) - 1)) % m


def key_generation(P, Q):
    N = int(P) * int(Q)
    φ = totient(N)
    E = mutually_prime_number(φ)  # генерируем Е, являеющееся взаимно-простым с функцией Эйлера от модуля N
    D = solve_comparison(E, φ)

    return D, E, N

def encryption(message, P, Q):
    message = message_to_pos_unicode(message)

    key = key_generation(P, Q)
    D = key[0]
    E = key[1]
    N = key[2]
    new_message = ''
    for i in message:
        new_message += '0' * (len(str(N)) - len(str((int(i) ** D) % N))) + str((int(i) ** D) % N)

    return new_message, E, N


def decryption(message, E, N):
    message = wrap(message, len(str(N)))
    new_message = []

    for i in message:
        new_message.append((int(i) ** E) % N)

    new_message = pos_unicode_to_message(new_message)

    return new_message


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def pos_unicode_to_message(message):
    new_message = ''
    for i in message:
        new_message += chr(i)

    return new_message


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))


message = input('Введите сообщение: ')
P_Q = list(map(int, input('Введите простые числа P и Q через пробел (значения параметров должны быть не меньше 30): ').split()))

if P_Q[0] < 30 or P_Q[1] < 30 or not is_prime(P_Q[0]) or not is_prime(P_Q[1]):
    print('Введите простые P и Q, большие 30.')
    sys.exit(0)

enc = encryption(message, P_Q[0], P_Q[1])
print(enc[0])

dec = decryption(enc[0], enc[1], enc[2])
print(dec)

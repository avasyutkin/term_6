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


def encryption(message, P_Q):
    P_Q = P_Q.split()

    if len(P_Q) < 2:
        return 'Введите два параметра P и Q.'

    if not P_Q[0].isnumeric():
        return 'Значение параметра P должно быть простым целым числом.'
    if not P_Q[1].isnumeric():
        return 'Значение параметра Q должно быть простым целым числом.'

    P = int(P_Q[0])
    Q = int(P_Q[1])

    if not is_prime(P):
        return 'Число Р должно быть простым.'

    if not is_prime(Q):
        return 'Число Q должно быть простым.'

    message = message_to_pos_unicode(message)

    key = key_generation(P, Q)
    D = key[0]
    E = key[1]
    N = key[2]
    new_message = ''
    for i in message:
        new_message += '0' * (len(str(N)) - len(str((int(i) ** E) % N))) + str((int(i) ** E) % N)

    return 'Зашифрованное сообщение: ' + new_message + '\nПараметры D и N: ' + str(D) + ' ' + str(N)


def decryption(message, D_N):
    D_N = D_N.split()

    if len(D_N) < 2:
        return 'Введите два параметра D и N.'

    if not D_N[0].isnumeric():
        return 'Значение параметра D должно быть целым числом.'
    if not D_N[1].isnumeric():
        return 'Значение параметра N должно быть целым числом.'

    D = int(D_N[0])
    N = int(D_N[1])

    message = wrap(message, len(str(N)))
    new_message = []

    for i in message:
        new_message.append((int(i) ** D) % N)

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

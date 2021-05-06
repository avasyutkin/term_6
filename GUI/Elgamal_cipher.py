import math
import random
from textwrap import wrap
import sys
from sympy.ntheory import totient


def solve_comparison(g, x, p):  # решаем сравнение

    return (g ** x) % p


def k_generation(φ, len_message):
    k_array = []

    while len(k_array) != len_message:
        a = random.randint(2, φ)
        while math.gcd(a, φ) != 1:   # проверка рандомизатора на взаимную простоту с функцией Эйлера от модуля
            a = random.randint(2, φ)
        k_array.append(a)

    return k_array


def encryption(message, P_G_X):
    P_G_X = P_G_X.split()

    if len(P_G_X) < 3:
        return 'Введите три параметра P, G и X.'

    if not P_G_X[0].isnumeric():
        return 'Значение параметра P должно быть целым числом.'
    if not P_G_X[1].isnumeric():
        return 'Значение параметра G должно быть целым числом.'
    if not P_G_X[2].isnumeric():
        return 'Значение параметра X должно быть целым числом.'

    p = int(P_G_X[0])
    g = int(P_G_X[1])
    x = int(P_G_X[2])

    if not is_prime(p):
        return 'Число Р должно быть простым.'
    if g >= p:
        return 'Значение параметра G должно быть меньше P.'
    if x >= p:
        return 'Значение параметра X должно быть меньше Р.'

    message = message_to_pos_unicode(message)
    k = k_generation(totient(p), len(message))
    y = solve_comparison(g, x, p)
    new_message = ''

    for i in range(len(message)):
        a = '0' * (len(str(p)) - len(str((g ** k[i]) % p))) + str((g ** k[i]) % p)
        b = '0' * (len(str(p)) - len(str((int(message[i]) * y ** k[i]) % p))) + str((int(message[i]) * y ** k[i]) % p)
        new_message += a + b

    return 'Зашифрованное сообщение: ' + new_message + '\nПараметры D и N: ' + str(x) + ' ' + str(p)


def decryption(message, x_p):
    x_p = x_p.split()

    if len(x_p) < 2:
        return 'Введите два параметра X и P.'

    if not x_p[0].isnumeric():
        return 'Значение параметра Y должно быть целым числом.'
    if not x_p[1].isnumeric():
        return 'Значение параметра G должно быть целым числом.'

    x, p = int(x_p[0]), int(x_p[1])


    message = wrap(message,len(str(p)))
    φ = totient(p) - 1
    new_message = []

    for i in range(0, len(message), 2):
        a = (int(message[i])**x) % p
        new_message.append((int(message[i+1]) * (a**φ)) % p)

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

"""
message = input('Введите сообщение: ')
print('Введите числа p — простое и большее', int(max(message_to_pos_unicode(message))), 'и g, x, меньшие p, через пробел: ')
p_g_x = list(map(int, input().split()))

if p_g_x[0] < int(max(message_to_pos_unicode(message))) or not is_prime(p_g_x[0]) or p_g_x[1] > p_g_x[0] or p_g_x[2] > p_g_x[0]:
    print('Введите корректные параметры.')
    sys.exit(0)

enc = encryption(message, p_g_x[1], p_g_x[2], p_g_x[0])
print(enc)

dec = decryption(enc,  p_g_x[2], p_g_x[0])
print(dec)
"""
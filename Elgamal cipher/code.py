import math
import random
from textwrap import wrap
import sys

def solve_comparison(g, x, p):  # решаем сравнение

    return (g ** x) % p


def euler_function(a):
    p = 0
    
    for i in range(a):
        if math.gcd(a, i) == 1:
            p += 1

    return p


def k_generation(φ, len_message):
    k_array = []

    while len(k_array) != len_message:
        a = random.randint(2, φ)
        while math.gcd(a, φ) != 1:
            a = random.randint(2, φ)
        k_array.append(a)

    return k_array


def encryption(message, g, x, p):
    message = message_to_pos_unicode(message)
    k = k_generation(euler_function(p), len(message))
    y = solve_comparison(g, x, p)
    new_message = ''

    for i in range(len(message)):
        a = '0' * (4 - len(str((g ** k[i]) % p))) + str((g ** k[i]) % p)
        b = '0' * (4 - len(str((int(message[i]) * y ** k[i]) % p))) + str((int(message[i]) * y ** k[i]) % p)
        new_message += a + b

    return new_message


def decryption(message, x, p):
    message = wrap(message, 4)
    φ = euler_function(p) - 1
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
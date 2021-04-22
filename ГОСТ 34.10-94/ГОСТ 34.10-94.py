from sympy.ntheory import totient
import random
import math
import sys


def hash_(message, p):
    h = 0
    hash = 0
    for i in message:
        hash = (h + int(i) + 1) ** 2 % p
        h = hash

    return hash


def solve_comparison(g, x, p):  # решаем сравнение

    return (g ** x) % p


def get_multiplier(n):
    num = random.randint(5, n)
    while n % num != 0 or not is_prime(num):
        num = random.randint(5, n)

    return num


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))


def get_a(q, p):  # генерация а
    a = random.randint(2, p - 1)
    while a ** q % p != 1:
        a = random.randint(2, p - 1)

    return a


def generation_signature(message, p):

    message_ = message_to_pos_unicode(message)
    h = hash_(message_, p)
    q = get_multiplier(p - 1)
    x = random.randint(2, q)  # генерация x
    a = get_a(q, p)
    y = solve_comparison(a, x, p)
    if h % q == 0:
        h = 1

    k = random.randint(2, q) # генерация k
    r = a ** k % p % q
    s = (x * r + k * h) % q
    while r == 0:
        k = random.randint(2, q)
        r = a ** k % p % q
        s = (x * r + k * h) % q

    return message, r, s, a, q, y, k


def signature_verification(message, p, q, a, r, s, y):
    message_ = message_to_pos_unicode(message)
    h = hash_(message_, p)

    v = h ** (q - 2) % q
    z1 = s * v % q
    z2 = (q - r) * v % q
    u = a ** z1 * y ** z2 % p % q

    if u == r:
        print('Подпись верна.')
    else:
        print('Подпись не верна. u и r:', u, r)



def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


message = input('Введите сообщение: ')
key = int(input('Введите простое p через пробел: '))

if not is_prime(key):
    print('Введите простое p.')
    sys.exit(0)

signature = generation_signature(message, key)
print('Сообщение и подпись:', signature[0:3])
print('Параметры a, q, y, k:', signature[3], signature[4], signature[5], signature[6])
print()

message = input("Введите сообщение: ")
key = list(map(int, input('Для проверки подписи введите через пробел p, q, a, r, s, y: ').split()))
signature_verification(message, key[0], key[1], key[2], key[3], key[4], key[5])

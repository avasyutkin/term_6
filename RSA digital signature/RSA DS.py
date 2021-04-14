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


def mutually_prime_number(a):   # ищем взаимно-простое число
    b = random.randint(2, 1000000)
    while math.gcd(a, b) != 1:
        b = random.randint(2, 1000000)

    return b


def solve_comparison(a, m):  # решаем сравнение

    return (a ** (totient(m) - 1)) % m


def generation_signature(message, P, Q):
    message_ = message_to_pos_unicode(message)
    N = P * Q
    φ = totient(N)
    E = mutually_prime_number(φ)  # генерируем Е, являеющееся взаимно-простым с функцией Эйлера от модуля N
    D = solve_comparison(E, φ)
    hash = hash_(message_, N)
    S = hash ** D % N

    return message, S, E, N


def signature_verification(message, S, E, N):
    message_ = message_to_pos_unicode(message)
    if hash_(message_, N) == S ** E % N:
        print('Подпись верна.')
    else:
        print('Подпись не верна. Ваш и расшифрованный хэши:', hash_(message_, N), S ** E % N)


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))


message = input("Введите сообщение: ")
P_Q = list(map(int, input('Введите простые числа P и Q через пробел: ').split()))

if not is_prime(P_Q[0]) or not is_prime(P_Q[1]):
    print('Введите простые P и Q.')
    sys.exit(0)

signature = generation_signature(message, P_Q[0], P_Q[1])
print('Сообщение и подпись:', signature[0:2])
print('Параметры E, N:', signature[2], signature[3])

print()
message = input("Введите сообщение: ")
S_E_N = list(map(int, input('Введите S, E, N: ').split()))

signature_verification(message, S_E_N[0], S_E_N[1], S_E_N[2])

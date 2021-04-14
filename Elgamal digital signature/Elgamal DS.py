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
    b = random.randint(2, a)
    while math.gcd(a, b) != 1:
        b = random.randint(2, a)

    return b


def generation_signature(message, P, G, X):
    Y = G ** X % P
    message_ = hash_(message_to_pos_unicode(message), P)
    K = mutually_prime_number(totient(P))  # генерируем K, являеющееся взаимно-простым с функцией Эйлера от модуля P
    print('Рандомизатор, взаимно простой с функцией Эйлера от модуля: ', K)
    a = G ** K % P
    b = solve_comparison(X, totient(P), a, message_, K)

    return message, a, b, Y


def signature_verification(message, a, b, Y, G, P):
    message_ = hash_(message_to_pos_unicode(message), P)
    A1 = ((Y ** a) * (a ** b)) % P
    A2 = G ** message_ % P
    if A1 == A2:
        print('Подпись верна.')
    else:
        print('Подпись не верна. A1 и A2:', A1, A2)


def solve_comparison(X, P, a, hash, K):  # решаем сравнение

    return ((hash - X * a) * K ** (totient(P) - 1)) % P


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))

message = input("Введите сообщение: ")
P_G_X = list(map(int, input('Введите простые числа P и G, меньшее Р, а также закрытый ключ, меньший Р-1, через пробел: ').split()))

if not is_prime(P_G_X[0]) or P_G_X[1] > P_G_X[0] or P_G_X[2] > P_G_X[0] - 1:
    print('Введите корректные параметры. Число Р должно быть простым, G - меньшим Р, а закрытый ключ - меньшим Р - 1.')
    sys.exit(0)

signature = generation_signature(message, P_G_X[0], P_G_X[1], P_G_X[2])
print('Сообщение и подпись:', signature[:3])
print('Параметр Y:', signature[3])
print()

message = input("Введите сообщение: ")
parameters = list(map(int, input('Введите a, b, Y, G, P: ').split()))

signature_verification(message, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])
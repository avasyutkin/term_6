from sympy.ntheory import totient
import random
import math


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


def generation_signature(message, P_G_X):
    P_G_X = P_G_X.split()

    if len(P_G_X) < 3:
        return 'Введите три параметра P, G и X.'

    if not P_G_X[0].isnumeric():
        return 'Значение параметра P должно быть целым числом.'
    if not P_G_X[1].isnumeric():
        return 'Значение параметра G должно быть целым числом.'
    if not P_G_X[2].isnumeric():
        return 'Значение параметра X должно быть целым числом.'

    P = int(P_G_X[0])
    G = int(P_G_X[1])
    X = int(P_G_X[2])

    if not is_prime(P):
        return 'Число Р должно быть простым.'
    if G >= P:
        return 'Значение параметра G должно быть меньше P.'
    if X >= P - 1:
        return 'Значение параметра X должно быть меньше Р-1.'

    Y = G ** X % P
    message_ = hash_(message_to_pos_unicode(message), P)
    K = mutually_prime_number(totient(P))  # генерируем K, являеющееся взаимно-простым с функцией Эйлера от модуля P

    a = G ** K % P
    b = solve_comparison(X, totient(P), a, message_, K)

    return 'Цифровая подпись: ' + str(a) + ' ' + str(b) + '\nЗначение параметра Y: ' + str(Y)


def signature_verification(message, a_b_Y_G_P):
    a_b_Y_G_P = a_b_Y_G_P.split()

    if len(a_b_Y_G_P) < 5:
        return 'Введите значение цифровой подписи (состоит из двух частей) и три параметра Y, G и P.'

    if not a_b_Y_G_P[0].isnumeric() or not a_b_Y_G_P[1].isnumeric():
        return 'Значение цифровой подписи представляет собой два целых числа.'
    if not a_b_Y_G_P[2].isnumeric():
        return 'Значение параметра Y должно быть целым числом.'
    if not a_b_Y_G_P[3].isnumeric():
        return 'Значение параметра G должно быть целым числом.'
    if not a_b_Y_G_P[4].isnumeric():
        return 'Значение параметра P должно быть целым числом.'
    if not is_prime(int(a_b_Y_G_P[4])):
        return 'Значение параметра P должно быть простым числом.'

    a, b, Y, G, P = int(a_b_Y_G_P[0]), int(a_b_Y_G_P[1]), int(a_b_Y_G_P[2]), int(a_b_Y_G_P[3]), int(a_b_Y_G_P[4])
    message_ = hash_(message_to_pos_unicode(message), P)
    A1 = ((Y ** a) * (a ** b)) % P
    A2 = G ** message_ % P

    if A1 == A2:
        return 'Подпись верна.'
    else:
        return 'Подпись не верна. A1 и A2: ' + str(A1) + ' ' + str(A2)


def solve_comparison(X, P, a, hash, K):  # решаем сравнение

    return ((hash - X * a) * K ** (totient(P) - 1)) % P


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))


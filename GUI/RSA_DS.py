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
    b = random.randint(2, 1000000)
    while math.gcd(a, b) != 1:
        b = random.randint(2, 1000000)

    return b


def solve_comparison(a, m):  # решаем сравнение

    return (a ** (totient(m) - 1)) % m


def generation_signature(message, P_Q):
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

    message_ = message_to_pos_unicode(message)
    N = P * Q
    φ = totient(N)
    E = mutually_prime_number(φ)  # генерируем Е, являеющееся взаимно-простым с функцией Эйлера от модуля N
    D = solve_comparison(E, φ)
    hash = hash_(message_, N)
    S = hash ** D % N

    return 'Цифровая подпись: ' + str(S) + '\nПараметры Е и N: ' + str(E) + ' ' + str(N)


def signature_verification(message, S_E_N):
    S_E_N = S_E_N.split()

    if len(S_E_N) < 3:
        return 'Введите значение цифровой подписи и два параметра E и N.'

    if not S_E_N[0].isnumeric():
        return 'Значение цифровой подписи должно быть целым числом.'
    if not S_E_N[1].isnumeric():
        return 'Значение параметра E должно быть целым числом.'
    if not S_E_N[2].isnumeric():
        return 'Значение параметра N должно быть целым числом.'

    S = int(S_E_N[0])
    E = int(S_E_N[1])
    N = int(S_E_N[2])

    message_ = message_to_pos_unicode(message)
    if hash_(message_, N) == S ** E % N:
        return 'Подпись верна.'
    else:
        return 'Подпись не верна. Ваш и расшифрованный хэши: ' + str(hash_(message_, N)) + ' ' + str(S ** E % N)


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))

import random


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
    p = p.split()[0]

    if not p.isnumeric():
        return 'Значение параметра p должно быть целым числом.'

    p = int(p)
    if p <= 22:
        return 'Значение параметра p должно быть больше 22.'

    if not is_prime(p):
        return 'Число p должно быть простым.'

    message_ = message_to_pos_unicode(message)
    h = hash_(message_, p)
    q = get_multiplier(p - 1)
    x = random.randint(2, q)  # генерация x
    a = get_a(q, p)
    y = solve_comparison(a, x, p)
    if h % q == 0:
        h = 1

    k = random.randint(2, q)  # генерация k
    r = a ** k % p % q
    s = (x * r + k * h) % q
    while r == 0:
        k = random.randint(2, q)
        r = a ** k % p % q
        s = (x * r + k * h) % q

    return 'Цифровая подпись: ' + str(r) + ' ' + str(s) + '\nЗначение параметров a, q, y: ' + str(a) + ' ' + str(q) + ' ' + str(y)


def signature_verification(message, r_s_p_q_a_y):
    r_s_p_q_a_y = r_s_p_q_a_y.split()

    if len(r_s_p_q_a_y) < 6:
        return 'Введите значение цифровой подписи (состоит из двух частей) и четыре параметра p, q, а и y.'

    if not r_s_p_q_a_y[0].isnumeric() or not r_s_p_q_a_y[1].isnumeric():
        return 'Значение цифровой подписи представляет собой два целых числа.'
    if not r_s_p_q_a_y[2].isnumeric():
        return 'Значение параметра p должно быть целым числом.'
    if not is_prime(int(r_s_p_q_a_y[2])):
        return 'Значение параметра p должно быть простым числом.'
    if not r_s_p_q_a_y[3].isnumeric():
        return 'Значение параметра q должно быть целым числом.'
    if not r_s_p_q_a_y[4].isnumeric():
        return 'Значение параметра a должно быть целым числом.'
    if not r_s_p_q_a_y[5].isnumeric():
        return 'Значение параметра y должно быть целым числом.'

    r, s, p, q, a, y = int(r_s_p_q_a_y[0]), int(r_s_p_q_a_y[1]), int(r_s_p_q_a_y[2]), int(r_s_p_q_a_y[3]), int(r_s_p_q_a_y[4]), int(r_s_p_q_a_y[5])

    message_ = message_to_pos_unicode(message)
    h = hash_(message_, p)

    v = h ** (q - 2) % q
    z1 = s * v % q
    z2 = (q - r) * v % q
    u = a ** z1 * y ** z2 % p % q

    if u == r:
        return 'Подпись верна.'
    else:
        return 'Подпись не верна. u и r: ' + str(u) + ' ' + str(r)


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


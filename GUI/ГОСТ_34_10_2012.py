import random
from sympy.ntheory import totient

def hash_(message, p):
    h = 0
    hash = 0
    for i in message:
        hash = (h + int(i) + 1) ** 2 % p
        h = hash

    return hash


def doubling_P(P, a, p):
    λ = ['', '']
    λ[0] = (3 * P[0] ** 2 + a) % p
    λ[1] = 2 * P[1] % p
    if λ[1] == 0:
        return 0
    if not (λ[0]/λ[1]).is_integer():
        λ[0] = λ[0] % p
        λ[1] = (λ[1] ** (totient(p) - 1)) % p
        λ = int(λ[0] * λ[1] % p)
    else:
        λ = int(λ[0]/λ[1])

    x = (λ ** 2 - 2 * P[0]) % p
    y = (λ * (P[0] - x) - P[1]) % p

    return x, y


def addition_P(P1, P2, p):
    λ = ['', '']
    λ[0] = (P2[1] - P1[1]) % p
    λ[1] = (P2[0] - P1[0]) % p
    if λ[1] == 0:
        return 0
    if not (λ[0]/λ[1]).is_integer():
        λ[0] = λ[0] % p
        λ[1] = (λ[1] ** (totient(p) - 1)) % p
        λ = int(λ[0] * λ[1] % p)
    else:
        λ = int(λ[0]/λ[1])

    x = (λ ** 2 - P1[0] - P2[0]) % p
    y = (λ * (P1[0] - x) - P1[1]) % p

    return x, y


def key_gen(P, k, a, p):
    k = bin(k)[3:]
    P_ = P
    for i in k:
        P_ = doubling_P(P_, a, p)

        if i == '1':
            P_ = addition_P(P, P_, p)

    return P_


def message_to_pos_unicode(message):
    new_message = []

    for i in message:
        new_message.append(('0' * (4 - len(str(ord(i)))) + str(ord(i))))

    return new_message


def generation_signature(message, xu_k):
    xu_k = xu_k.split()
    if len(xu_k) < 2:
        return 'Введите секретный ключ и рандомизатор.'
    if not xu_k[0].isnumeric():
        return 'Значение секретного ключа должно быть целым числом.'
    if not xu_k[1].isnumeric():
        return 'Значение рандомизатора должно быть целым числом.'

    curves = [[2005, 7935, 8537, [7625, 3580], 127], [7270, 8322, 9137, [8189, 3901], 61], [5596, 1413, 9967, [2093, 4157], 229]]
    curve = random.choice(curves)
    a = curve[0]
    p = curve[2]
    G = curve[3]
    q = curve[4]

    xu = int(xu_k[0]) % p
    k = int(xu_k[1]) % p

    message_ = message_to_pos_unicode(message)
    hash = hash_(message_, q)

    if hash == 0:
        hash = 1

    yu = key_gen(G, xu, a, p)
    P = key_gen(G, k, a, p)

    r = P[0] % q
    s = (k * hash + r * xu) % q
    return 'Введенное сообщение подписано парой чисел: ' + str(r) + ' ' + str(s) + '\nПараметры эллиптической кривой: a = ' + str(a) + '  p = ' + str(p) + '  q = ' + str(q) + '  G = ' + str(G) + '\nОткрытый ключ: ' + str(yu)



def signature_verification(message, r_s_yu_a_p_q_G):
    r_s_yu_a_p_q_G = r_s_yu_a_p_q_G.split()
    if len(r_s_yu_a_p_q_G) < 9:
        return 'Введите значение цифровой подписи (r, s), открытый ключ (yu) и параметры кривой (a, p, q, G).'
    if not r_s_yu_a_p_q_G[0].isnumeric() or not r_s_yu_a_p_q_G[1].isnumeric():
        return 'Значение цифровой подписи представляет собой два целых числа.'
    if not r_s_yu_a_p_q_G[2].isnumeric() or not r_s_yu_a_p_q_G[3].isnumeric():
        return 'Значение открытого ключа должно быть целым числом.'
    if not r_s_yu_a_p_q_G[4].isnumeric() or not r_s_yu_a_p_q_G[5].isnumeric() or not r_s_yu_a_p_q_G[6].isnumeric() or not r_s_yu_a_p_q_G[7].isnumeric() or not r_s_yu_a_p_q_G[8].isnumeric():
        return 'Параметры кривой должны быть целыми числами.'

    r, s, a, p, q = int(r_s_yu_a_p_q_G[0]), int(r_s_yu_a_p_q_G[1]), int(r_s_yu_a_p_q_G[4]), int(r_s_yu_a_p_q_G[5]), int(r_s_yu_a_p_q_G[6])
    yu = []
    G = []
    yu.append(int(r_s_yu_a_p_q_G[2]))
    yu.append(int(r_s_yu_a_p_q_G[3]))
    G.append(int(r_s_yu_a_p_q_G[7]))
    G.append(int(r_s_yu_a_p_q_G[8]))


    if r < 0 or r > q or s < 0 or s > q:
        return 'Параметры s и r должны быть больше 0 и меньше ' + str(q)

    message_ = message_to_pos_unicode(message)
    hash = hash_(message_, q)
    if hash == 0:
        hash = 1

    u1 = s * hash ** (totient(q) - 1) % q
    u2 = (-r * hash ** (totient(q) - 1)) % q

    P1 = key_gen(G, u1, a, p)
    P2 = key_gen(yu, u2, a, p)
    P = addition_P(P1, P2, p)

    if P[0] % q == r:
        return 'Подпись верна.'
    else:
        return 'Подпись не верна. xp mod q = ' + ' ' + str(P[0] % q) + ' и r = ' + str(r)


def is_prime(a):  # проверка простоты числа

    return all(a % i for i in range(2, a))

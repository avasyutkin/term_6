import math
import random
from sympy.ntheory import totient

alphabet_dec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']


def euler_function(a):
    p = 0

    for i in range(a):
        if math.gcd(a, i) == 1:
            p += 1

    return p


def doubling_P(P, a, p):
    λ = ['', '']
    λ[0] = (3 * P[0] ** 2 + a) % p
    λ[1] = 2 * P[1] % p

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


def encryption(message, Cb):
    if not Cb.isnumeric():
        return 'Значение ключа должно быть целым числом.'
    Cb = int(Cb)
    if Cb > 65537:
        return 'Секретный ключ не должен превышать 65537.'

    message = message_to_pos_unicode(message)
    new_message = ''
    P = generation_P()

    for i in range(len(message)):
        k = generation_k()
        public_key = key_gen(P, Cb, a, p)
        private_key = key_gen(P, k, a, p)
        P = key_gen(public_key, k, a, p)

        new_message += str(private_key[0]) + ' ' + str(private_key[1]) + ' ' + str(int(message[i]) * P[0] % p) + ' '

    return new_message


def decryption(message, Cb):
    if not Cb.isnumeric():
        return 'Значение ключа должно быть целым числом.'
    Cb = int(Cb)
    if Cb > 65537:
        return 'Секретный ключ не должен превышать 65537.'

    for i in message:
        if i not in alphabet_dec:
            return 'Введенное сообщение не является шифртекстом.'

    message = message.split()
    new_message = []
    for i in range(0, len(message), 3):
        message_ = []
        message_.append((int(message[i]), int(message[i+1])))

        P = key_gen(message_[0], Cb, a, p)
        new_message.append(int(message[i+2]) * (P[0] ** (p - 2)) % p)

    new_message = pos_unicode_to_message(new_message)

    return new_message


def generation_k():

    return random.randint(2, p)  # !!! должно быть до q - порядок точки G


def generation_P():
    x = random.randint(-p, p)
    y = random.choice([(x ** 3 + a * x + b) % p, (x ** 3 + a * x + b) % p])

    return x, y


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



a = 1282
b = 26572
p = 65537

"""
message = input('Введите сообщение: ')
key = int(input('Введите закрытый ключ (число не больше 65537):  '))

enc = encryption(message, key)
print('Зашифрованное сообщение:', enc)

dec = decryption(enc, key)
print('Расшифрованное сообщение:', dec)
"""
import math
import sys
import random
from sympy.ntheory import totient

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


def encryption(message, P, Cb):
    message = message_to_pos_unicode(message)
    new_message = []

    for i in range(len(message)):
        k = generation_k()
        public_key = key_gen(P, Cb, a, p)
        private_key = key_gen(P, k, a, p)
        P = key_gen(public_key, k, a, p)

        new_message.append(private_key)
        new_message.append(str(int(message[i]) * P[0] % p))


    return new_message


def decryption(message, Cb):
    new_message = []
    for i in range(0, len(message), 2):
        P = key_gen(message[i], Cb, a, p)

        new_message.append(int(message[i+1]) * (P[0] ** (p - 2)) % p)

    new_message = pos_unicode_to_message(new_message)

    return new_message


def generation_k():

    return random.randint(2, p)


def generation_P():
    x = random.randint(2, p)

    return x, (x ** 3 + a * x + b) % p


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


def curve_check(a, x_y, p):
    if a < p:
        b = ((x_y[1] ** 2) - ((x_y[0] ** 3) + (a * x_y[0]))) % p

        if (4 * (a ** 3) + 27 * (b ** 2)) % p == 0:
            b = ((x_y[1] ** 2) - ((x_y[0] ** 3) + (a * x_y[0]))) % p
            return b

        else:
            print('Ваша кривая является особенной. Введите другие параметры, или вы можете воспользоваться кривой, предоставленной по умолчанию.')
            sys.exit(0)

    else:
        print('Ввденный параметр а больше модуля p. Введите другие параметры, или вы можете воспользоваться кривой, предоставленной по умолчанию.')
        sys.exit(0)




a = 1282
b = 26572
p = 65537

message = input('Введите сообщение: ')
choice = input('Хотите ввести параметры кривой? Если нет, вы сможете воспользоваться встроенной. (Да / Нет) ')
if choice == 'Нет':
    print('Кривая: y^2 = x^3 +', a, '* x +', b, 'mod', p)
    key = int(input('Введите закрытый ключ (число не больше 65537):  '))
    x_y = generation_P()
    if key > 65537:
        print('Введите новый ключ, меньший 65537.')
        sys.exit(0)

elif choice == 'Да':
    a = int(input('Введите а: '))
    p = int(input('Введите p: '))
    x_y = generation_P()
    b = curve_check(a, x_y, p)
    print('Кривая: y^2 = x^3 +', a, '* x +', b, 'mod', p)
    key = int(input('Введите закрытый ключ (число не больше 65537):  '))
else:
    print('Перезапустите программу и выберите Да / Нет.')
    sys.exit(0)

enc = encryption(message, x_y, key)
print('Закрытый ключ и зашифрованное сообщение:', enc)

dec = decryption(enc, key)
print('Расшифрованное сообщение:', dec)